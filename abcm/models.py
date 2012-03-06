# -*- coding: utf-8 -*-
# Copyright (C) 2012  Alejandro Varas

# This file is part of abcm.

# abcm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GNU Emacs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with abmc.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models


class Meeting(models.Model):
    main_objective = models.TextField("Objetivo Principal")
    date_time = models.DateTimeField("Fecha y hora")
    convener_name = models.ForeignKey('auth.user', verbose_name="Nombre Convocante", related_name="mettings_created")
    objectives = models.TextField("Obejetivos de la reunión", help_text="Listado de objetivos específicos")
    meeting_type = models.ManyToManyField('MeetingType', verbose_name="Tipo de reunión")
    participants = models.ManyToManyField('auth.user', verbose_name="Participantes")

    def __unicode__(self):
        return self.main_objective[:80]

class MeetingType(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name
