package Utilities.DBConnection;

import java.sql.Connection;
public interface IDBConnection {
    boolean ConnectToServer();
    boolean DisconnectFromServer();
    Connection GetConnection();
}
