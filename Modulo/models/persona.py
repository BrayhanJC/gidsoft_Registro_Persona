# -*- coding: utf-8 -*-

from osv import osv, fields

class autor(osv.Model):
	_name='gidsoft.peliculas.autor'
	_rec_name='nom_autor'

	cbo_sexo=[
		('M', 'Masculino'),
		('F', 'Femenino'),
		('I', 'Indeterminado')
	]

	_columns={
		'name':fields.char('Nombre Integrante', size=32),
		'identificacion':fields.integer('Identificacion', required=True, size=10),		
		'sexo':fields.selection(cbo_sexo, 'Sexo'),
		'fecha_nacimiento':fields.date('Fecha de nacimiento'),
		'edad':fields.integer('Edad', size=3),
		
		'pais':fields.selection(cbo_pais, 'Pais de origen')
	}