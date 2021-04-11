import json
import logging
import logging.handlers

from scripts.documents.document_manager import DocumentManager
from scripts.error.error_manager import ErrorManager
from scripts.progress.progress_manager import ProgressManager


class BasicApp(object):
    """The basic application"""

    def __init__(self, configuration_filename):
        """Initializes the application="""
        self.configuration_filename = configuration_filename
        self.main_configuration = self.__get_configuration()
        self.application_name = self.__init_application_name()
        self.logger = self.__init_logger()
        try:
            self.document_manager = self.__init_document_manager()
        except Exception as exp:
            raise exp
        self.progress_manager = self.__init_progress_manager()
        self.error_manager = ErrorManager()

    # ===== PRIVATE METHODS =====

    def __get_configuration(self):
        """Reads configuration file"""
        json_data = open(self.configuration_filename)
        data = json.load(json_data)
        return data

    def __init_application_name(self):
        """Gets the application name from the configuration file"""
        main_configuration = self.main_configuration
        application_configuration = main_configuration["application_configuration"]
        application_name = application_configuration["application_name"]
        return application_name

    def __init_logger(self):
        """Configures and initializes logger"""
        main_configuration = self.main_configuration
        logger_configuration = main_configuration["logger_configuration"]
        format = logger_configuration["format"]
        logging.basicConfig(format=format)
        logger = logging.getLogger(self.get_application_name())
        logger.setLevel(logging.DEBUG)
        file_handler = self.__get_file_handler()
        logger.addHandler(file_handler)
        return logger

    def __get_file_handler(self):
        """Opens file and sets as stream for logging"""
        file_handler = None
        if file_handler is None:
            try:
                file_handler = logging.FileHandler("logs/" + self.get_application_name() + ".log")
            except:
                pass
        if file_handler is None:
            try:
                file_handler = logging.FileHandler("../logs/" + self.get_application_name() + ".log")
            except:
                pass
        file_handler.setLevel(logging.DEBUG)
        return file_handler

    def __init_document_manager(self):
        """Initializes database manager from the configuration file"""
        database_configuration = self.main_configuration["database_configuration"]
        document_manager = DocumentManager(database_configuration)
        return document_manager

    def __init_progress_manager(self):
        """Initializes progress manager"""
        progress_manager = ProgressManager(self.logger)
        progress_manager.activate()
        return progress_manager

    # ===== PUBLIC METHODS =====

    def get_application_name(self):
        return self.application_name

    def get_smtp_handler(self):
        main_configuration = self.main_configuration
        smtp_handler_configuration = main_configuration["smtp_handler_configuration"]
        mailhost = smtp_handler_configuration["mailhost"]
        fromaddr = smtp_handler_configuration["fromaddr"]
        toaddrs = smtp_handler_configuration["toaddrs"]
        subject = self.application_name + ' : ' + smtp_handler_configuration["subject"]
        user = smtp_handler_configuration["user"]
        pwd = smtp_handler_configuration["pwd"]
        smtp_handler = logging.handlers.SMTPHandler(mailhost=mailhost,
                                                    fromaddr=fromaddr,
                                                    toaddrs=toaddrs,
                                                    subject=subject,
                                                    credentials=(user, pwd),
                                                    secure=())
        smtp_handler.setLevel(logging.INFO)
        return smtp_handler

    def step(self):
        self.progress_manager.step()

    def process(self):
        pass

    def start(self):
        self.logger.info("App started: " + self.get_application_name())
        try:
            self.process()
        except IOError as e:
            self.error_manager.add(e.strerror)
        except Exception as e:
            self.error_manager.add(e)
        self.logger.info("App finished: " + self.get_application_name())
        if self.error_manager.is_errors_exist():
            errors = self.error_manager.errors.exceptions
            self.logger.critical(str(len(errors)) + " error(s)!")
            for error in errors:
                self.logger.critical("Error: " + str(error))
