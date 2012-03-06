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

from django.contrib import admin

from abcm.forms import MeetingAdminForm
from abcm.models import Meeting, MeetingType


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('convener_name', 'date_time', 'main_objective')

admin.site.register(Meeting, MeetingAdmin)

admin.site.register(MeetingType)


