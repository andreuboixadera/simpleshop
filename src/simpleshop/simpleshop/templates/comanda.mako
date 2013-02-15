# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Productes</h1>

<ul id="tasks">
% if tasks:
  <form method="post">
  % for task in tasks:
  <li>
    <b><span class="name">${task['nom']}</span></b><br>
    <!--<span class="name">${task['stock']} unitats</span>-->
    <span class="name">${task['preu']} €</span>
    <br><br> Quantitat a comprar: <input type="text" id="${task['id']}" value="0" maxlength="4" size="3" > 
  </li>
  % endfor
  <br><input type="submit" name="add" value="Realitzar commanda" class="button"><br>
 </form>
% else:
  <li>No hi han productes</li>
% endif
</ul>
