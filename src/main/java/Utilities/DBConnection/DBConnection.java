package Utilities.DBConnection;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

import Utilities.LoggerManager.LoggerManager;

public class DBConnection implements IDBConnection {
    private String URL;
    private String User;
    private String Password;
    // 使用单例模式，instance即单例
    private static DBConnection instance = null;
    private Connection connection = null;

    public static synchronized DBConnection GetInstance(){
        if(instance == null)
            instance = new DBConnection();
        return instance;
    }
    public DBConnection(){
        this.LoadDBConfig();
    }
    @Override
    public boolean ConnectToServer() {
        try{
            this.connection = DriverManager.getConnection(URL,User,Password);
            LoggerManager.DatabaseLogger.info("connected to server : " + this.URL);
            return true;
        }
        catch (SQLException E){
            LoggerManager.DatabaseLogger.info("failed to connect to server : " + this.URL+" , and reason is "+ E.toString());
            return false;
        }
    }
    @Override
    public boolean DisconnectFromServer() {
        if(this.connection != null){
            try{
                this.connection.close();
                LoggerManager.DatabaseLogger.info(this.URL + " has been closed");
                this.connection = null;
                return true;
            }catch (SQLException E){
                LoggerManager.DatabaseLogger.warn(this.URL + " can not be closed");
                this.connection = null;
                return false;
            }
        }else{
            LoggerManager.DatabaseLogger.warn("connection with " + this.URL + "has not been made, can not disconnect");
            return false;
        }
    }
    @Override
    public Connection GetConnection() {
        if(this.connection != null)
            return this.connection;
        else {
            LoggerManager.DatabaseLogger.warn("connection with server has not been established");
            return null;
        }
    }

    private void LoadDBConfig(){
        Properties DbProperty = new Properties();
        try(FileInputStream input = new FileInputStream("properties/dbconfig.properties")){
            DbProperty.load(input);
            this.URL = DbProperty.getProperty("db.url");
            this.Password = DbProperty.getProperty("db.password");
            this.User = DbProperty.getProperty("db.user");
            LoggerManager.DatabaseLogger.info("successfully load dbconfig file");
        }
        catch (IOException e){
            LoggerManager.DatabaseLogger.error("Failed to load dbconfig file");
        }

    }
}
