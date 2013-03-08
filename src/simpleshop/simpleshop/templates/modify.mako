# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Modificar producte</h1>

<form method="post">
<table>
  <tr>Nom Producte  <tr><input type="text" maxlength="50" name="nom"><br>
  <tr>Quantitat disp  <tr><input type="text" maxlength="10" name="quantitat"><br>
  <tr>Preu producte  <tr><input type="text" maxlength="10" name="preu"><br></br>
  <input type="submit" name="modificar" value="Modificar producte" class="button"><br>
</table>
  <br><li> <a href="/simpleshop/admin">Llista productes</a>
</form>
