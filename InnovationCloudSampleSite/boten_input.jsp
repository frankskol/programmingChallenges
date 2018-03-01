<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>LKW einfügen</title>
</head>
<body>
   <form action="truck_insert.jsp" method="post">
     <table border="0">
       <tr>
        <td>Seriennummer:</td>
        <td><input type="text" name="serienNr" /></td>
       </tr>
       <tr>
        <td>Baujahr:</td>
        <td><input type="text" name="baujahr" /></td>
       </tr>
       <tr>
        <td>Kaufpreis:</td>
        <td><input type="text" name="kaufPreis" /></td>
       </tr>
       <tr>
        <td>Zulässige Nutzlast:</td>
        <td><input type="text" name="zulaessigeNutzlast" /></td>
       </tr>
       <tr>
        <td>Kilometerstand:</td>
        <td><input type="text" name="kmStand" /></td>
       </tr>
       <tr>
        <td>Letztes Service:</td>
        <td><input type="text" name="letztesService" /> (yyyy-mm-dd)</td>
       </tr>
       <tr>
        <td>Letzter Ölwechsel:</td>
        <td><input type="text" name="letzterOelwechsel" /> (yyyy-mm-dd)</td>
       </tr>
     </table>
     
     <input type="submit" value="Insert"/>
   </form>
  <br />
  <a href="index.htm">Zur Startseite</a>
</body>
</html>