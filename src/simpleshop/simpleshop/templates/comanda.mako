# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<a href=/simpleshop/admin style="float:right">Administracio</a>
<h1>Productes</h1>

<ul id="tasks">
% if tasks:
  <form method="post">
  <h4>Comanda <input disabled id="idComanda" value="${idcomanda}" style="width:40px" ></h4>
  % for task in tasks:
  <li>
    <b><span class="nom">${task['nom']}</span></b><br>
    <!--<span class="name">${task['stock']} unitats</span>-->
    <span class="preu">${task['preu']} €</span>
    <br><br> Quantitat a comprar: <input type="text" name="${task['id']}" value="0" maxlength="4" size="3" > 
  </li><hr />
  % endfor
  <br><input type="submit" name="add" value="Realitzar commanda" class="button"><br>
 </form>
% else:
  <li>No hi han productes</li>
% endif
</ul><br />

