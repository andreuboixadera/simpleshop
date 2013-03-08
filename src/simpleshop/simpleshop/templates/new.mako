# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Nou producte</h1>

<form action="${request.route_url('new')}" method="post">
  _ID_ Producte <input type="text" maxlength="20" name="id" required><br></br>
  Nom Producte <input type="text" maxlength="50" name="nom" required><br>
  Quantitat disp <input type="text" maxlength="10" name="quantitat" required><br>
  Preu producte <input type="text" maxlength="10" name="preu" required><br></br>
  <input type="submit" name="add" value="Affegir producte" class="button"><br>
  <br><li> <a href="${request.route_url('list')}">Llista productes</a>
</form>
