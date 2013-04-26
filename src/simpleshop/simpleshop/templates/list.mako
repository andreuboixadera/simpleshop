# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<a href="comandas"><span style="position:relative; float:right;">Comandes&nbsp&nbsp&nbsp</span></a>
<h1>Productes</h1>

<ul id="tasks">
% if tasks:
  % for task in tasks:
  <li>
    <b><span class="name">${task['nom']}</span></b><br>
    <span class="name">${task['stock']} unitats</span>
    <span class="name">${task['preu']} €</span>
    <span class="actions">	
    </span>
	<div id="separador" align="right">
	[<a href="${request.route_url('modify', id=task['id'])}">Modificar</a>]
	[<a href="${request.route_url('close', id=task['id'])}">Eliminar</a>]	</div>
  </li>
  % endfor
% else:
  <li>No hi han productes</li>
% endif
  <li class="last">
    <a href="${request.route_url('new')}">Affegir producte</a></li>
  <br />
  <li class="last">
    <a href="${request.route_url('buy')}">Area client</a></li>
  
</ul>
