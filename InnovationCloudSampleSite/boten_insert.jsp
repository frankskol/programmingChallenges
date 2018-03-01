<%@page import="javax.sql.DataSource"%>
<%@page import="javax.naming.Context"%>
<%@page import="javax.naming.InitialContext"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.Date"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Boten einfügen</title>
</head>
<body>
  <%
    // get a connection from the DataSource       	
	Context initContext = new InitialContext();	  
	DataSource ds = (DataSource)initContext.lookup("java:/comp/env/jdbc/myoracle");
	Connection con = ds.getConnection();
    
	con.setAutoCommit(false);

    // delete the truck with the specified serial number
    String query = "INSERT INTO lkw(serienNr, baujahr, kaufPreis, zulaessigeNutzlast, kmStand, letztesService, letzterOelwechsel)" + 
        " VALUES(?,?,?,?,?,?,?)";
       
    PreparedStatement stmt = null;
    ResultSet rs = null;
    
    try {
      int serienNr = Integer.parseInt(request.getParameter("serienNr"));
      int baujahr = Integer.parseInt(request.getParameter("baujahr"));
      double kaufPreis = Double.parseDouble(request.getParameter("kaufPreis"));
      double zulaessigeNutzlast = Double.parseDouble(request.getParameter("zulaessigeNutzlast"));
      int kmStand = Integer.parseInt(request.getParameter("kmStand"));
      Date letztesService = null;
      Date letzterOelwechsel = null;
      
      if (request.getParameter("letztesService") != null && 
    	  !request.getParameter("letztesService").equals("")) {
          // @tricky: Wenn das Eingabefeld leer ist, dann ist letztesService nicht null, sondern "";
          letztesService = Date.valueOf(request.getParameter("letztesService"));
      }
      
      if (request.getParameter("letzterOelwechsel") != null && 
          !request.getParameter("letzterOelwechsel").equals("")) {
          letzterOelwechsel = Date.valueOf(request.getParameter("letzterOelwechsel"));
      }
        
      stmt = con.prepareStatement(query);
      
      // bind variables
      stmt.setInt(1, serienNr);
      stmt.setInt(2, baujahr);
      stmt.setDouble(3, kaufPreis);
      stmt.setDouble(4, zulaessigeNutzlast);
      stmt.setInt(5, kmStand);
      
      if(letztesService != null)
      	  stmt.setDate(6, letztesService);
      else
      	  stmt.setNull(6, java.sql.Types.DATE); // NULL value allowed
      
      if(letzterOelwechsel != null)
      	  stmt.setDate(7, letzterOelwechsel);
      else
          stmt.setNull(7, java.sql.Types.DATE); // NULL value allowed
      
      stmt.executeUpdate();

      // commit the changes
      con.commit();
      
      out.println("Der LKW mit der Seriennummer " + serienNr + " wurde erfolgreich eingefügt!");
    } catch(SQLException e) {
      out.println("Error: " + e.getMessage());
      con.rollback();
      e.printStackTrace();
    } catch(Exception e) {
      out.println("Error: " + e.getMessage());
      con.rollback();
      e.printStackTrace();
    } finally {    
 	   // Always make sure result sets and statements are closed,
 	   // and the connection is returned to the pool
 	   if (rs != null) {
 	      try { rs.close(); } catch (SQLException e) { ; }
 	      rs = null;
 	    }
 	    if (stmt != null) {
 	      try { stmt.close(); } catch (SQLException e) { ; }
 	      stmt = null;
 	    }
 	    if (con != null) {
 	      try { con.close(); } catch (SQLException e) { ; }
 	      con = null;
 	    }
    }
  %>
  <br />
  <a href="truck_overview.jsp">Zur LKW-Übersicht</a>

</body>
</html>