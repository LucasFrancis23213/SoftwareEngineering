package Utilities.LoggerManager;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class LoggerManager {
    public static final Logger GlobalLogger = LoggerFactory.getLogger("GlobalLogger");
    public static final Logger ServiceLogger = LoggerFactory.getLogger("ServiceLogger");
    public static final Logger DatabaseLogger = LoggerFactory.getLogger("DatabaseLogger");
    public static final Logger ControllerLogger = LoggerFactory.getLogger("ControllerLogger");
    public static void add_Log(){
        GlobalLogger.error("error 1");
        GlobalLogger.warn("warn 2");
        ServiceLogger.warn("warn 3");
        ServiceLogger.error("error 4");
        DatabaseLogger.warn("test db warning");
        ControllerLogger.warn("test controller");
    }

}
