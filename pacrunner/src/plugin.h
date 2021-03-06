/*
 *
 *  PACrunner - Proxy configuration daemon
 *
 *  Copyright (C) 2010-2011  Intel Corporation. All rights reserved.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License version 2 as
 *  published by the Free Software Foundation.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 */

struct pacrunner_plugin_desc {
	const char *name;
	int (*init) (void);
	void (*exit) (void);
};

#define PACRUNNER_BUILTIN_PLUGIN_DEFINE(name, init, exit) \
		struct pacrunner_plugin_desc __pacrunner_builtin_ ## name = { \
			#name, init, exit \
		};

#ifdef PACRUNNER_PLUGIN_BUILTIN
#define PACRUNNER_PLUGIN_DEFINE PACRUNNER_BUILTIN_PLUGIN_DEFINE
#else
#define PACRUNNER_PLUGIN_DEFINE(name, init, exit) \
		extern struct pacrunner_plugin_desc pacrunner_plugin_desc \
				__attribute__ ((visibility("default"))); \
		struct pacrunner_plugin_desc pacrunner_plugin_desc = { \
			#name, init, exit \
		};
#endif
