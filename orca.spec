#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : orca
Version  : 3.32.0
Release  : 18
URL      : https://download.gnome.org/sources/orca/3.32/orca-3.32.0.tar.xz
Source0  : https://download.gnome.org/sources/orca/3.32/orca-3.32.0.tar.xz
Summary  : Screen reader for individuals who are blind or visually impaired
Group    : Development/Tools
License  : LGPL-2.1
Requires: orca-bin = %{version}-%{release}
Requires: orca-data = %{version}-%{release}
Requires: orca-license = %{version}-%{release}
Requires: orca-locales = %{version}-%{release}
Requires: orca-man = %{version}-%{release}
Requires: orca-python = %{version}-%{release}
Requires: orca-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(atk-bridge-2.0)
BuildRequires : pkgconfig(atspi-2)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pygobject

%description
Orca v3.32.0
Introduction
========================================================================

%package bin
Summary: bin components for the orca package.
Group: Binaries
Requires: orca-data = %{version}-%{release}
Requires: orca-license = %{version}-%{release}

%description bin
bin components for the orca package.


%package data
Summary: data components for the orca package.
Group: Data

%description data
data components for the orca package.


%package doc
Summary: doc components for the orca package.
Group: Documentation
Requires: orca-man = %{version}-%{release}

%description doc
doc components for the orca package.


%package license
Summary: license components for the orca package.
Group: Default

%description license
license components for the orca package.


%package locales
Summary: locales components for the orca package.
Group: Default

%description locales
locales components for the orca package.


%package man
Summary: man components for the orca package.
Group: Default

%description man
man components for the orca package.


%package python
Summary: python components for the orca package.
Group: Default
Requires: orca-python3 = %{version}-%{release}

%description python
python components for the orca package.


%package python3
Summary: python3 components for the orca package.
Group: Default
Requires: python3-core

%description python3
python3 components for the orca package.


%prep
%setup -q -n orca-3.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557021859
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557021859
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/orca
cp COPYING %{buildroot}/usr/share/package-licenses/orca/COPYING
cp icons/COPYING %{buildroot}/usr/share/package-licenses/orca/icons_COPYING
%make_install
%find_lang orca

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/orca

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/16x16/apps/orca.png
/usr/share/icons/hicolor/22x22/apps/orca.png
/usr/share/icons/hicolor/24x24/apps/orca.png
/usr/share/icons/hicolor/32x32/apps/orca.png
/usr/share/icons/hicolor/48x48/apps/orca.png
/usr/share/icons/hicolor/scalable/apps/orca.svg
/usr/share/icons/hicolor/symbolic/apps/orca-symbolic.svg
/usr/share/orca/ui/orca-find.ui
/usr/share/orca/ui/orca-setup.ui

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/orca/commands.page
/usr/share/help/C/orca/commands_bookmarks.page
/usr/share/help/C/orca/commands_braille.page
/usr/share/help/C/orca/commands_chat.page
/usr/share/help/C/orca/commands_controlling_orca.page
/usr/share/help/C/orca/commands_debugging.page
/usr/share/help/C/orca/commands_find.page
/usr/share/help/C/orca/commands_flat_review.page
/usr/share/help/C/orca/commands_live_regions.page
/usr/share/help/C/orca/commands_mouse.page
/usr/share/help/C/orca/commands_profiles.page
/usr/share/help/C/orca/commands_reading.page
/usr/share/help/C/orca/commands_speech_settings.page
/usr/share/help/C/orca/commands_structural_navigation.page
/usr/share/help/C/orca/commands_table.page
/usr/share/help/C/orca/commands_time_date_notifications.page
/usr/share/help/C/orca/commands_where_am_i.page
/usr/share/help/C/orca/figures/orca-logo.png
/usr/share/help/C/orca/howto_bookmarks.page
/usr/share/help/C/orca/howto_documents.page
/usr/share/help/C/orca/howto_flat_review.page
/usr/share/help/C/orca/howto_forms.page
/usr/share/help/C/orca/howto_key_bindings.page
/usr/share/help/C/orca/howto_keyboard_layout.page
/usr/share/help/C/orca/howto_learn_modes.page
/usr/share/help/C/orca/howto_live_regions.page
/usr/share/help/C/orca/howto_mouse_review.page
/usr/share/help/C/orca/howto_notifications.page
/usr/share/help/C/orca/howto_orca_find.page
/usr/share/help/C/orca/howto_profiles.page
/usr/share/help/C/orca/howto_setting_up_orca.page
/usr/share/help/C/orca/howto_structural_navigation.page
/usr/share/help/C/orca/howto_tables.page
/usr/share/help/C/orca/howto_text_attributes.page
/usr/share/help/C/orca/howto_the_orca_modifier.page
/usr/share/help/C/orca/howto_toggling_caps_lock.page
/usr/share/help/C/orca/howto_whereami.page
/usr/share/help/C/orca/index.page
/usr/share/help/C/orca/introduction.page
/usr/share/help/C/orca/preferences.page
/usr/share/help/C/orca/preferences_braille.page
/usr/share/help/C/orca/preferences_chat.page
/usr/share/help/C/orca/preferences_gecko.page
/usr/share/help/C/orca/preferences_general.page
/usr/share/help/C/orca/preferences_introduction.page
/usr/share/help/C/orca/preferences_key_bindings.page
/usr/share/help/C/orca/preferences_key_echo.page
/usr/share/help/C/orca/preferences_pronunciation.page
/usr/share/help/C/orca/preferences_speech.page
/usr/share/help/C/orca/preferences_spellcheck.page
/usr/share/help/C/orca/preferences_table_navigation.page
/usr/share/help/C/orca/preferences_text_attributes.page
/usr/share/help/C/orca/preferences_voice.page
/usr/share/help/bg/orca/commands.page
/usr/share/help/bg/orca/commands_bookmarks.page
/usr/share/help/bg/orca/commands_braille.page
/usr/share/help/bg/orca/commands_chat.page
/usr/share/help/bg/orca/commands_controlling_orca.page
/usr/share/help/bg/orca/commands_debugging.page
/usr/share/help/bg/orca/commands_find.page
/usr/share/help/bg/orca/commands_flat_review.page
/usr/share/help/bg/orca/commands_live_regions.page
/usr/share/help/bg/orca/commands_mouse.page
/usr/share/help/bg/orca/commands_profiles.page
/usr/share/help/bg/orca/commands_reading.page
/usr/share/help/bg/orca/commands_speech_settings.page
/usr/share/help/bg/orca/commands_structural_navigation.page
/usr/share/help/bg/orca/commands_table.page
/usr/share/help/bg/orca/commands_time_date_notifications.page
/usr/share/help/bg/orca/commands_where_am_i.page
/usr/share/help/bg/orca/figures/orca-logo.png
/usr/share/help/bg/orca/howto_bookmarks.page
/usr/share/help/bg/orca/howto_documents.page
/usr/share/help/bg/orca/howto_flat_review.page
/usr/share/help/bg/orca/howto_forms.page
/usr/share/help/bg/orca/howto_key_bindings.page
/usr/share/help/bg/orca/howto_keyboard_layout.page
/usr/share/help/bg/orca/howto_learn_modes.page
/usr/share/help/bg/orca/howto_live_regions.page
/usr/share/help/bg/orca/howto_mouse_review.page
/usr/share/help/bg/orca/howto_notifications.page
/usr/share/help/bg/orca/howto_orca_find.page
/usr/share/help/bg/orca/howto_profiles.page
/usr/share/help/bg/orca/howto_setting_up_orca.page
/usr/share/help/bg/orca/howto_structural_navigation.page
/usr/share/help/bg/orca/howto_tables.page
/usr/share/help/bg/orca/howto_text_attributes.page
/usr/share/help/bg/orca/howto_the_orca_modifier.page
/usr/share/help/bg/orca/howto_toggling_caps_lock.page
/usr/share/help/bg/orca/howto_whereami.page
/usr/share/help/bg/orca/index.page
/usr/share/help/bg/orca/introduction.page
/usr/share/help/bg/orca/preferences.page
/usr/share/help/bg/orca/preferences_braille.page
/usr/share/help/bg/orca/preferences_chat.page
/usr/share/help/bg/orca/preferences_gecko.page
/usr/share/help/bg/orca/preferences_general.page
/usr/share/help/bg/orca/preferences_introduction.page
/usr/share/help/bg/orca/preferences_key_bindings.page
/usr/share/help/bg/orca/preferences_key_echo.page
/usr/share/help/bg/orca/preferences_pronunciation.page
/usr/share/help/bg/orca/preferences_speech.page
/usr/share/help/bg/orca/preferences_spellcheck.page
/usr/share/help/bg/orca/preferences_table_navigation.page
/usr/share/help/bg/orca/preferences_text_attributes.page
/usr/share/help/bg/orca/preferences_voice.page
/usr/share/help/cs/orca/commands.page
/usr/share/help/cs/orca/commands_bookmarks.page
/usr/share/help/cs/orca/commands_braille.page
/usr/share/help/cs/orca/commands_chat.page
/usr/share/help/cs/orca/commands_controlling_orca.page
/usr/share/help/cs/orca/commands_debugging.page
/usr/share/help/cs/orca/commands_find.page
/usr/share/help/cs/orca/commands_flat_review.page
/usr/share/help/cs/orca/commands_live_regions.page
/usr/share/help/cs/orca/commands_mouse.page
/usr/share/help/cs/orca/commands_profiles.page
/usr/share/help/cs/orca/commands_reading.page
/usr/share/help/cs/orca/commands_speech_settings.page
/usr/share/help/cs/orca/commands_structural_navigation.page
/usr/share/help/cs/orca/commands_table.page
/usr/share/help/cs/orca/commands_time_date_notifications.page
/usr/share/help/cs/orca/commands_where_am_i.page
/usr/share/help/cs/orca/figures/orca-logo.png
/usr/share/help/cs/orca/howto_bookmarks.page
/usr/share/help/cs/orca/howto_documents.page
/usr/share/help/cs/orca/howto_flat_review.page
/usr/share/help/cs/orca/howto_forms.page
/usr/share/help/cs/orca/howto_key_bindings.page
/usr/share/help/cs/orca/howto_keyboard_layout.page
/usr/share/help/cs/orca/howto_learn_modes.page
/usr/share/help/cs/orca/howto_live_regions.page
/usr/share/help/cs/orca/howto_mouse_review.page
/usr/share/help/cs/orca/howto_notifications.page
/usr/share/help/cs/orca/howto_orca_find.page
/usr/share/help/cs/orca/howto_profiles.page
/usr/share/help/cs/orca/howto_setting_up_orca.page
/usr/share/help/cs/orca/howto_structural_navigation.page
/usr/share/help/cs/orca/howto_tables.page
/usr/share/help/cs/orca/howto_text_attributes.page
/usr/share/help/cs/orca/howto_the_orca_modifier.page
/usr/share/help/cs/orca/howto_toggling_caps_lock.page
/usr/share/help/cs/orca/howto_whereami.page
/usr/share/help/cs/orca/index.page
/usr/share/help/cs/orca/introduction.page
/usr/share/help/cs/orca/preferences.page
/usr/share/help/cs/orca/preferences_braille.page
/usr/share/help/cs/orca/preferences_chat.page
/usr/share/help/cs/orca/preferences_gecko.page
/usr/share/help/cs/orca/preferences_general.page
/usr/share/help/cs/orca/preferences_introduction.page
/usr/share/help/cs/orca/preferences_key_bindings.page
/usr/share/help/cs/orca/preferences_key_echo.page
/usr/share/help/cs/orca/preferences_pronunciation.page
/usr/share/help/cs/orca/preferences_speech.page
/usr/share/help/cs/orca/preferences_spellcheck.page
/usr/share/help/cs/orca/preferences_table_navigation.page
/usr/share/help/cs/orca/preferences_text_attributes.page
/usr/share/help/cs/orca/preferences_voice.page
/usr/share/help/de/orca/commands.page
/usr/share/help/de/orca/commands_bookmarks.page
/usr/share/help/de/orca/commands_braille.page
/usr/share/help/de/orca/commands_chat.page
/usr/share/help/de/orca/commands_controlling_orca.page
/usr/share/help/de/orca/commands_debugging.page
/usr/share/help/de/orca/commands_find.page
/usr/share/help/de/orca/commands_flat_review.page
/usr/share/help/de/orca/commands_live_regions.page
/usr/share/help/de/orca/commands_mouse.page
/usr/share/help/de/orca/commands_profiles.page
/usr/share/help/de/orca/commands_reading.page
/usr/share/help/de/orca/commands_speech_settings.page
/usr/share/help/de/orca/commands_structural_navigation.page
/usr/share/help/de/orca/commands_table.page
/usr/share/help/de/orca/commands_time_date_notifications.page
/usr/share/help/de/orca/commands_where_am_i.page
/usr/share/help/de/orca/figures/orca-logo.png
/usr/share/help/de/orca/howto_bookmarks.page
/usr/share/help/de/orca/howto_documents.page
/usr/share/help/de/orca/howto_flat_review.page
/usr/share/help/de/orca/howto_forms.page
/usr/share/help/de/orca/howto_key_bindings.page
/usr/share/help/de/orca/howto_keyboard_layout.page
/usr/share/help/de/orca/howto_learn_modes.page
/usr/share/help/de/orca/howto_live_regions.page
/usr/share/help/de/orca/howto_mouse_review.page
/usr/share/help/de/orca/howto_notifications.page
/usr/share/help/de/orca/howto_orca_find.page
/usr/share/help/de/orca/howto_profiles.page
/usr/share/help/de/orca/howto_setting_up_orca.page
/usr/share/help/de/orca/howto_structural_navigation.page
/usr/share/help/de/orca/howto_tables.page
/usr/share/help/de/orca/howto_text_attributes.page
/usr/share/help/de/orca/howto_the_orca_modifier.page
/usr/share/help/de/orca/howto_toggling_caps_lock.page
/usr/share/help/de/orca/howto_whereami.page
/usr/share/help/de/orca/index.page
/usr/share/help/de/orca/introduction.page
/usr/share/help/de/orca/preferences.page
/usr/share/help/de/orca/preferences_braille.page
/usr/share/help/de/orca/preferences_chat.page
/usr/share/help/de/orca/preferences_gecko.page
/usr/share/help/de/orca/preferences_general.page
/usr/share/help/de/orca/preferences_introduction.page
/usr/share/help/de/orca/preferences_key_bindings.page
/usr/share/help/de/orca/preferences_key_echo.page
/usr/share/help/de/orca/preferences_pronunciation.page
/usr/share/help/de/orca/preferences_speech.page
/usr/share/help/de/orca/preferences_spellcheck.page
/usr/share/help/de/orca/preferences_table_navigation.page
/usr/share/help/de/orca/preferences_text_attributes.page
/usr/share/help/de/orca/preferences_voice.page
/usr/share/help/el/orca/commands.page
/usr/share/help/el/orca/commands_bookmarks.page
/usr/share/help/el/orca/commands_braille.page
/usr/share/help/el/orca/commands_chat.page
/usr/share/help/el/orca/commands_controlling_orca.page
/usr/share/help/el/orca/commands_debugging.page
/usr/share/help/el/orca/commands_find.page
/usr/share/help/el/orca/commands_flat_review.page
/usr/share/help/el/orca/commands_live_regions.page
/usr/share/help/el/orca/commands_mouse.page
/usr/share/help/el/orca/commands_profiles.page
/usr/share/help/el/orca/commands_reading.page
/usr/share/help/el/orca/commands_speech_settings.page
/usr/share/help/el/orca/commands_structural_navigation.page
/usr/share/help/el/orca/commands_table.page
/usr/share/help/el/orca/commands_time_date_notifications.page
/usr/share/help/el/orca/commands_where_am_i.page
/usr/share/help/el/orca/figures/orca-logo.png
/usr/share/help/el/orca/howto_bookmarks.page
/usr/share/help/el/orca/howto_documents.page
/usr/share/help/el/orca/howto_flat_review.page
/usr/share/help/el/orca/howto_forms.page
/usr/share/help/el/orca/howto_key_bindings.page
/usr/share/help/el/orca/howto_keyboard_layout.page
/usr/share/help/el/orca/howto_learn_modes.page
/usr/share/help/el/orca/howto_live_regions.page
/usr/share/help/el/orca/howto_mouse_review.page
/usr/share/help/el/orca/howto_notifications.page
/usr/share/help/el/orca/howto_orca_find.page
/usr/share/help/el/orca/howto_profiles.page
/usr/share/help/el/orca/howto_setting_up_orca.page
/usr/share/help/el/orca/howto_structural_navigation.page
/usr/share/help/el/orca/howto_tables.page
/usr/share/help/el/orca/howto_text_attributes.page
/usr/share/help/el/orca/howto_the_orca_modifier.page
/usr/share/help/el/orca/howto_toggling_caps_lock.page
/usr/share/help/el/orca/howto_whereami.page
/usr/share/help/el/orca/index.page
/usr/share/help/el/orca/introduction.page
/usr/share/help/el/orca/preferences.page
/usr/share/help/el/orca/preferences_braille.page
/usr/share/help/el/orca/preferences_chat.page
/usr/share/help/el/orca/preferences_gecko.page
/usr/share/help/el/orca/preferences_general.page
/usr/share/help/el/orca/preferences_introduction.page
/usr/share/help/el/orca/preferences_key_bindings.page
/usr/share/help/el/orca/preferences_key_echo.page
/usr/share/help/el/orca/preferences_pronunciation.page
/usr/share/help/el/orca/preferences_speech.page
/usr/share/help/el/orca/preferences_spellcheck.page
/usr/share/help/el/orca/preferences_table_navigation.page
/usr/share/help/el/orca/preferences_text_attributes.page
/usr/share/help/el/orca/preferences_voice.page
/usr/share/help/es/orca/commands.page
/usr/share/help/es/orca/commands_bookmarks.page
/usr/share/help/es/orca/commands_braille.page
/usr/share/help/es/orca/commands_chat.page
/usr/share/help/es/orca/commands_controlling_orca.page
/usr/share/help/es/orca/commands_debugging.page
/usr/share/help/es/orca/commands_find.page
/usr/share/help/es/orca/commands_flat_review.page
/usr/share/help/es/orca/commands_live_regions.page
/usr/share/help/es/orca/commands_mouse.page
/usr/share/help/es/orca/commands_profiles.page
/usr/share/help/es/orca/commands_reading.page
/usr/share/help/es/orca/commands_speech_settings.page
/usr/share/help/es/orca/commands_structural_navigation.page
/usr/share/help/es/orca/commands_table.page
/usr/share/help/es/orca/commands_time_date_notifications.page
/usr/share/help/es/orca/commands_where_am_i.page
/usr/share/help/es/orca/figures/orca-logo.png
/usr/share/help/es/orca/howto_bookmarks.page
/usr/share/help/es/orca/howto_documents.page
/usr/share/help/es/orca/howto_flat_review.page
/usr/share/help/es/orca/howto_forms.page
/usr/share/help/es/orca/howto_key_bindings.page
/usr/share/help/es/orca/howto_keyboard_layout.page
/usr/share/help/es/orca/howto_learn_modes.page
/usr/share/help/es/orca/howto_live_regions.page
/usr/share/help/es/orca/howto_mouse_review.page
/usr/share/help/es/orca/howto_notifications.page
/usr/share/help/es/orca/howto_orca_find.page
/usr/share/help/es/orca/howto_profiles.page
/usr/share/help/es/orca/howto_setting_up_orca.page
/usr/share/help/es/orca/howto_structural_navigation.page
/usr/share/help/es/orca/howto_tables.page
/usr/share/help/es/orca/howto_text_attributes.page
/usr/share/help/es/orca/howto_the_orca_modifier.page
/usr/share/help/es/orca/howto_toggling_caps_lock.page
/usr/share/help/es/orca/howto_whereami.page
/usr/share/help/es/orca/index.page
/usr/share/help/es/orca/introduction.page
/usr/share/help/es/orca/preferences.page
/usr/share/help/es/orca/preferences_braille.page
/usr/share/help/es/orca/preferences_chat.page
/usr/share/help/es/orca/preferences_gecko.page
/usr/share/help/es/orca/preferences_general.page
/usr/share/help/es/orca/preferences_introduction.page
/usr/share/help/es/orca/preferences_key_bindings.page
/usr/share/help/es/orca/preferences_key_echo.page
/usr/share/help/es/orca/preferences_pronunciation.page
/usr/share/help/es/orca/preferences_speech.page
/usr/share/help/es/orca/preferences_spellcheck.page
/usr/share/help/es/orca/preferences_table_navigation.page
/usr/share/help/es/orca/preferences_text_attributes.page
/usr/share/help/es/orca/preferences_voice.page
/usr/share/help/fr/orca/commands.page
/usr/share/help/fr/orca/commands_bookmarks.page
/usr/share/help/fr/orca/commands_braille.page
/usr/share/help/fr/orca/commands_chat.page
/usr/share/help/fr/orca/commands_controlling_orca.page
/usr/share/help/fr/orca/commands_debugging.page
/usr/share/help/fr/orca/commands_find.page
/usr/share/help/fr/orca/commands_flat_review.page
/usr/share/help/fr/orca/commands_live_regions.page
/usr/share/help/fr/orca/commands_mouse.page
/usr/share/help/fr/orca/commands_profiles.page
/usr/share/help/fr/orca/commands_reading.page
/usr/share/help/fr/orca/commands_speech_settings.page
/usr/share/help/fr/orca/commands_structural_navigation.page
/usr/share/help/fr/orca/commands_table.page
/usr/share/help/fr/orca/commands_time_date_notifications.page
/usr/share/help/fr/orca/commands_where_am_i.page
/usr/share/help/fr/orca/figures/orca-logo.png
/usr/share/help/fr/orca/howto_bookmarks.page
/usr/share/help/fr/orca/howto_documents.page
/usr/share/help/fr/orca/howto_flat_review.page
/usr/share/help/fr/orca/howto_forms.page
/usr/share/help/fr/orca/howto_key_bindings.page
/usr/share/help/fr/orca/howto_keyboard_layout.page
/usr/share/help/fr/orca/howto_learn_modes.page
/usr/share/help/fr/orca/howto_live_regions.page
/usr/share/help/fr/orca/howto_mouse_review.page
/usr/share/help/fr/orca/howto_notifications.page
/usr/share/help/fr/orca/howto_orca_find.page
/usr/share/help/fr/orca/howto_profiles.page
/usr/share/help/fr/orca/howto_setting_up_orca.page
/usr/share/help/fr/orca/howto_structural_navigation.page
/usr/share/help/fr/orca/howto_tables.page
/usr/share/help/fr/orca/howto_text_attributes.page
/usr/share/help/fr/orca/howto_the_orca_modifier.page
/usr/share/help/fr/orca/howto_toggling_caps_lock.page
/usr/share/help/fr/orca/howto_whereami.page
/usr/share/help/fr/orca/index.page
/usr/share/help/fr/orca/introduction.page
/usr/share/help/fr/orca/preferences.page
/usr/share/help/fr/orca/preferences_braille.page
/usr/share/help/fr/orca/preferences_chat.page
/usr/share/help/fr/orca/preferences_gecko.page
/usr/share/help/fr/orca/preferences_general.page
/usr/share/help/fr/orca/preferences_introduction.page
/usr/share/help/fr/orca/preferences_key_bindings.page
/usr/share/help/fr/orca/preferences_key_echo.page
/usr/share/help/fr/orca/preferences_pronunciation.page
/usr/share/help/fr/orca/preferences_speech.page
/usr/share/help/fr/orca/preferences_spellcheck.page
/usr/share/help/fr/orca/preferences_table_navigation.page
/usr/share/help/fr/orca/preferences_text_attributes.page
/usr/share/help/fr/orca/preferences_voice.page
/usr/share/help/gl/orca/commands.page
/usr/share/help/gl/orca/commands_bookmarks.page
/usr/share/help/gl/orca/commands_braille.page
/usr/share/help/gl/orca/commands_chat.page
/usr/share/help/gl/orca/commands_controlling_orca.page
/usr/share/help/gl/orca/commands_debugging.page
/usr/share/help/gl/orca/commands_find.page
/usr/share/help/gl/orca/commands_flat_review.page
/usr/share/help/gl/orca/commands_live_regions.page
/usr/share/help/gl/orca/commands_mouse.page
/usr/share/help/gl/orca/commands_profiles.page
/usr/share/help/gl/orca/commands_reading.page
/usr/share/help/gl/orca/commands_speech_settings.page
/usr/share/help/gl/orca/commands_structural_navigation.page
/usr/share/help/gl/orca/commands_table.page
/usr/share/help/gl/orca/commands_time_date_notifications.page
/usr/share/help/gl/orca/commands_where_am_i.page
/usr/share/help/gl/orca/figures/orca-logo.png
/usr/share/help/gl/orca/howto_bookmarks.page
/usr/share/help/gl/orca/howto_documents.page
/usr/share/help/gl/orca/howto_flat_review.page
/usr/share/help/gl/orca/howto_forms.page
/usr/share/help/gl/orca/howto_key_bindings.page
/usr/share/help/gl/orca/howto_keyboard_layout.page
/usr/share/help/gl/orca/howto_learn_modes.page
/usr/share/help/gl/orca/howto_live_regions.page
/usr/share/help/gl/orca/howto_mouse_review.page
/usr/share/help/gl/orca/howto_notifications.page
/usr/share/help/gl/orca/howto_orca_find.page
/usr/share/help/gl/orca/howto_profiles.page
/usr/share/help/gl/orca/howto_setting_up_orca.page
/usr/share/help/gl/orca/howto_structural_navigation.page
/usr/share/help/gl/orca/howto_tables.page
/usr/share/help/gl/orca/howto_text_attributes.page
/usr/share/help/gl/orca/howto_the_orca_modifier.page
/usr/share/help/gl/orca/howto_toggling_caps_lock.page
/usr/share/help/gl/orca/howto_whereami.page
/usr/share/help/gl/orca/index.page
/usr/share/help/gl/orca/introduction.page
/usr/share/help/gl/orca/preferences.page
/usr/share/help/gl/orca/preferences_braille.page
/usr/share/help/gl/orca/preferences_chat.page
/usr/share/help/gl/orca/preferences_gecko.page
/usr/share/help/gl/orca/preferences_general.page
/usr/share/help/gl/orca/preferences_introduction.page
/usr/share/help/gl/orca/preferences_key_bindings.page
/usr/share/help/gl/orca/preferences_key_echo.page
/usr/share/help/gl/orca/preferences_pronunciation.page
/usr/share/help/gl/orca/preferences_speech.page
/usr/share/help/gl/orca/preferences_spellcheck.page
/usr/share/help/gl/orca/preferences_table_navigation.page
/usr/share/help/gl/orca/preferences_text_attributes.page
/usr/share/help/gl/orca/preferences_voice.page
/usr/share/help/hu/orca/commands.page
/usr/share/help/hu/orca/commands_bookmarks.page
/usr/share/help/hu/orca/commands_braille.page
/usr/share/help/hu/orca/commands_chat.page
/usr/share/help/hu/orca/commands_controlling_orca.page
/usr/share/help/hu/orca/commands_debugging.page
/usr/share/help/hu/orca/commands_find.page
/usr/share/help/hu/orca/commands_flat_review.page
/usr/share/help/hu/orca/commands_live_regions.page
/usr/share/help/hu/orca/commands_mouse.page
/usr/share/help/hu/orca/commands_profiles.page
/usr/share/help/hu/orca/commands_reading.page
/usr/share/help/hu/orca/commands_speech_settings.page
/usr/share/help/hu/orca/commands_structural_navigation.page
/usr/share/help/hu/orca/commands_table.page
/usr/share/help/hu/orca/commands_time_date_notifications.page
/usr/share/help/hu/orca/commands_where_am_i.page
/usr/share/help/hu/orca/figures/orca-logo.png
/usr/share/help/hu/orca/howto_bookmarks.page
/usr/share/help/hu/orca/howto_documents.page
/usr/share/help/hu/orca/howto_flat_review.page
/usr/share/help/hu/orca/howto_forms.page
/usr/share/help/hu/orca/howto_key_bindings.page
/usr/share/help/hu/orca/howto_keyboard_layout.page
/usr/share/help/hu/orca/howto_learn_modes.page
/usr/share/help/hu/orca/howto_live_regions.page
/usr/share/help/hu/orca/howto_mouse_review.page
/usr/share/help/hu/orca/howto_notifications.page
/usr/share/help/hu/orca/howto_orca_find.page
/usr/share/help/hu/orca/howto_profiles.page
/usr/share/help/hu/orca/howto_setting_up_orca.page
/usr/share/help/hu/orca/howto_structural_navigation.page
/usr/share/help/hu/orca/howto_tables.page
/usr/share/help/hu/orca/howto_text_attributes.page
/usr/share/help/hu/orca/howto_the_orca_modifier.page
/usr/share/help/hu/orca/howto_toggling_caps_lock.page
/usr/share/help/hu/orca/howto_whereami.page
/usr/share/help/hu/orca/index.page
/usr/share/help/hu/orca/introduction.page
/usr/share/help/hu/orca/preferences.page
/usr/share/help/hu/orca/preferences_braille.page
/usr/share/help/hu/orca/preferences_chat.page
/usr/share/help/hu/orca/preferences_gecko.page
/usr/share/help/hu/orca/preferences_general.page
/usr/share/help/hu/orca/preferences_introduction.page
/usr/share/help/hu/orca/preferences_key_bindings.page
/usr/share/help/hu/orca/preferences_key_echo.page
/usr/share/help/hu/orca/preferences_pronunciation.page
/usr/share/help/hu/orca/preferences_speech.page
/usr/share/help/hu/orca/preferences_spellcheck.page
/usr/share/help/hu/orca/preferences_table_navigation.page
/usr/share/help/hu/orca/preferences_text_attributes.page
/usr/share/help/hu/orca/preferences_voice.page
/usr/share/help/pt_BR/orca/commands.page
/usr/share/help/pt_BR/orca/commands_bookmarks.page
/usr/share/help/pt_BR/orca/commands_braille.page
/usr/share/help/pt_BR/orca/commands_chat.page
/usr/share/help/pt_BR/orca/commands_controlling_orca.page
/usr/share/help/pt_BR/orca/commands_debugging.page
/usr/share/help/pt_BR/orca/commands_find.page
/usr/share/help/pt_BR/orca/commands_flat_review.page
/usr/share/help/pt_BR/orca/commands_live_regions.page
/usr/share/help/pt_BR/orca/commands_mouse.page
/usr/share/help/pt_BR/orca/commands_profiles.page
/usr/share/help/pt_BR/orca/commands_reading.page
/usr/share/help/pt_BR/orca/commands_speech_settings.page
/usr/share/help/pt_BR/orca/commands_structural_navigation.page
/usr/share/help/pt_BR/orca/commands_table.page
/usr/share/help/pt_BR/orca/commands_time_date_notifications.page
/usr/share/help/pt_BR/orca/commands_where_am_i.page
/usr/share/help/pt_BR/orca/figures/orca-logo.png
/usr/share/help/pt_BR/orca/howto_bookmarks.page
/usr/share/help/pt_BR/orca/howto_documents.page
/usr/share/help/pt_BR/orca/howto_flat_review.page
/usr/share/help/pt_BR/orca/howto_forms.page
/usr/share/help/pt_BR/orca/howto_key_bindings.page
/usr/share/help/pt_BR/orca/howto_keyboard_layout.page
/usr/share/help/pt_BR/orca/howto_learn_modes.page
/usr/share/help/pt_BR/orca/howto_live_regions.page
/usr/share/help/pt_BR/orca/howto_mouse_review.page
/usr/share/help/pt_BR/orca/howto_notifications.page
/usr/share/help/pt_BR/orca/howto_orca_find.page
/usr/share/help/pt_BR/orca/howto_profiles.page
/usr/share/help/pt_BR/orca/howto_setting_up_orca.page
/usr/share/help/pt_BR/orca/howto_structural_navigation.page
/usr/share/help/pt_BR/orca/howto_tables.page
/usr/share/help/pt_BR/orca/howto_text_attributes.page
/usr/share/help/pt_BR/orca/howto_the_orca_modifier.page
/usr/share/help/pt_BR/orca/howto_toggling_caps_lock.page
/usr/share/help/pt_BR/orca/howto_whereami.page
/usr/share/help/pt_BR/orca/index.page
/usr/share/help/pt_BR/orca/introduction.page
/usr/share/help/pt_BR/orca/preferences.page
/usr/share/help/pt_BR/orca/preferences_braille.page
/usr/share/help/pt_BR/orca/preferences_chat.page
/usr/share/help/pt_BR/orca/preferences_gecko.page
/usr/share/help/pt_BR/orca/preferences_general.page
/usr/share/help/pt_BR/orca/preferences_introduction.page
/usr/share/help/pt_BR/orca/preferences_key_bindings.page
/usr/share/help/pt_BR/orca/preferences_key_echo.page
/usr/share/help/pt_BR/orca/preferences_pronunciation.page
/usr/share/help/pt_BR/orca/preferences_speech.page
/usr/share/help/pt_BR/orca/preferences_spellcheck.page
/usr/share/help/pt_BR/orca/preferences_table_navigation.page
/usr/share/help/pt_BR/orca/preferences_text_attributes.page
/usr/share/help/pt_BR/orca/preferences_voice.page
/usr/share/help/sl/orca/commands.page
/usr/share/help/sl/orca/commands_bookmarks.page
/usr/share/help/sl/orca/commands_braille.page
/usr/share/help/sl/orca/commands_chat.page
/usr/share/help/sl/orca/commands_controlling_orca.page
/usr/share/help/sl/orca/commands_debugging.page
/usr/share/help/sl/orca/commands_find.page
/usr/share/help/sl/orca/commands_flat_review.page
/usr/share/help/sl/orca/commands_live_regions.page
/usr/share/help/sl/orca/commands_mouse.page
/usr/share/help/sl/orca/commands_profiles.page
/usr/share/help/sl/orca/commands_reading.page
/usr/share/help/sl/orca/commands_speech_settings.page
/usr/share/help/sl/orca/commands_structural_navigation.page
/usr/share/help/sl/orca/commands_table.page
/usr/share/help/sl/orca/commands_time_date_notifications.page
/usr/share/help/sl/orca/commands_where_am_i.page
/usr/share/help/sl/orca/figures/orca-logo.png
/usr/share/help/sl/orca/howto_bookmarks.page
/usr/share/help/sl/orca/howto_documents.page
/usr/share/help/sl/orca/howto_flat_review.page
/usr/share/help/sl/orca/howto_forms.page
/usr/share/help/sl/orca/howto_key_bindings.page
/usr/share/help/sl/orca/howto_keyboard_layout.page
/usr/share/help/sl/orca/howto_learn_modes.page
/usr/share/help/sl/orca/howto_live_regions.page
/usr/share/help/sl/orca/howto_mouse_review.page
/usr/share/help/sl/orca/howto_notifications.page
/usr/share/help/sl/orca/howto_orca_find.page
/usr/share/help/sl/orca/howto_profiles.page
/usr/share/help/sl/orca/howto_setting_up_orca.page
/usr/share/help/sl/orca/howto_structural_navigation.page
/usr/share/help/sl/orca/howto_tables.page
/usr/share/help/sl/orca/howto_text_attributes.page
/usr/share/help/sl/orca/howto_the_orca_modifier.page
/usr/share/help/sl/orca/howto_toggling_caps_lock.page
/usr/share/help/sl/orca/howto_whereami.page
/usr/share/help/sl/orca/index.page
/usr/share/help/sl/orca/introduction.page
/usr/share/help/sl/orca/preferences.page
/usr/share/help/sl/orca/preferences_braille.page
/usr/share/help/sl/orca/preferences_chat.page
/usr/share/help/sl/orca/preferences_gecko.page
/usr/share/help/sl/orca/preferences_general.page
/usr/share/help/sl/orca/preferences_introduction.page
/usr/share/help/sl/orca/preferences_key_bindings.page
/usr/share/help/sl/orca/preferences_key_echo.page
/usr/share/help/sl/orca/preferences_pronunciation.page
/usr/share/help/sl/orca/preferences_speech.page
/usr/share/help/sl/orca/preferences_spellcheck.page
/usr/share/help/sl/orca/preferences_table_navigation.page
/usr/share/help/sl/orca/preferences_text_attributes.page
/usr/share/help/sl/orca/preferences_voice.page
/usr/share/help/sv/orca/commands.page
/usr/share/help/sv/orca/commands_bookmarks.page
/usr/share/help/sv/orca/commands_braille.page
/usr/share/help/sv/orca/commands_chat.page
/usr/share/help/sv/orca/commands_controlling_orca.page
/usr/share/help/sv/orca/commands_debugging.page
/usr/share/help/sv/orca/commands_find.page
/usr/share/help/sv/orca/commands_flat_review.page
/usr/share/help/sv/orca/commands_live_regions.page
/usr/share/help/sv/orca/commands_mouse.page
/usr/share/help/sv/orca/commands_profiles.page
/usr/share/help/sv/orca/commands_reading.page
/usr/share/help/sv/orca/commands_speech_settings.page
/usr/share/help/sv/orca/commands_structural_navigation.page
/usr/share/help/sv/orca/commands_table.page
/usr/share/help/sv/orca/commands_time_date_notifications.page
/usr/share/help/sv/orca/commands_where_am_i.page
/usr/share/help/sv/orca/figures/orca-logo.png
/usr/share/help/sv/orca/howto_bookmarks.page
/usr/share/help/sv/orca/howto_documents.page
/usr/share/help/sv/orca/howto_flat_review.page
/usr/share/help/sv/orca/howto_forms.page
/usr/share/help/sv/orca/howto_key_bindings.page
/usr/share/help/sv/orca/howto_keyboard_layout.page
/usr/share/help/sv/orca/howto_learn_modes.page
/usr/share/help/sv/orca/howto_live_regions.page
/usr/share/help/sv/orca/howto_mouse_review.page
/usr/share/help/sv/orca/howto_notifications.page
/usr/share/help/sv/orca/howto_orca_find.page
/usr/share/help/sv/orca/howto_profiles.page
/usr/share/help/sv/orca/howto_setting_up_orca.page
/usr/share/help/sv/orca/howto_structural_navigation.page
/usr/share/help/sv/orca/howto_tables.page
/usr/share/help/sv/orca/howto_text_attributes.page
/usr/share/help/sv/orca/howto_the_orca_modifier.page
/usr/share/help/sv/orca/howto_toggling_caps_lock.page
/usr/share/help/sv/orca/howto_whereami.page
/usr/share/help/sv/orca/index.page
/usr/share/help/sv/orca/introduction.page
/usr/share/help/sv/orca/preferences.page
/usr/share/help/sv/orca/preferences_braille.page
/usr/share/help/sv/orca/preferences_chat.page
/usr/share/help/sv/orca/preferences_gecko.page
/usr/share/help/sv/orca/preferences_general.page
/usr/share/help/sv/orca/preferences_introduction.page
/usr/share/help/sv/orca/preferences_key_bindings.page
/usr/share/help/sv/orca/preferences_key_echo.page
/usr/share/help/sv/orca/preferences_pronunciation.page
/usr/share/help/sv/orca/preferences_speech.page
/usr/share/help/sv/orca/preferences_spellcheck.page
/usr/share/help/sv/orca/preferences_table_navigation.page
/usr/share/help/sv/orca/preferences_text_attributes.page
/usr/share/help/sv/orca/preferences_voice.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/orca/COPYING
/usr/share/package-licenses/orca/icons_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/orca.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f orca.lang
%defattr(-,root,root,-)

