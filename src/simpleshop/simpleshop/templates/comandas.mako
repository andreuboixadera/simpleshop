# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<a href=/admin style="float:right; margin-rigth:0;">Administracio</a>
<a href="buy"><span style="position:relative; float:right;">Llista Productes&nbsp&nbsp&nbsp</span></a>
<h1>Comandes</h1>

<ul id="tasks">
% if tasks:
</ul>
  % for task in tasks:
	<li>
		${task['contingut']}
	</li>

  % endfor

% else:
  <li>No hi han comandes</li>
% endif

  
</ul>
