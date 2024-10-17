Name:		grhino
Version:	0.16.1
Release:	2
Summary:	An Othello/Reversi chess with strong AI
License:	GPLv2+
Group:		Games/Boards
URL:		https://rhino.sourceforge.net/
Source:		http://downloads.sourceforge.net/rhino/%{name}-%{version}.tar.gz
Patch0:		grhino-0.16.0-gcc43.patch
Patch1:		grhino-0.16.0-mdv-fix-str-fmt.patch
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
GRhino, or Rhino its former name, is an Othello/Reversi game on Linux
and other UNIX-like systems. What distinguish GRhino from most other
Othello games is that GRhino will be targeted for experienced Othello
players. Strong AI is the main focus and the ultimate target strength
of the AI is that it should be able to beat the best human player at
the highest difficulty level.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .strfmt

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Comment=Othello/Reversi chess with strong AI
Categories=BoardGame;Game;GTK;GNOME;
Name=GRhino
EOF

%find_lang %{name} --with-gnome --all-name

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc README
%{_gamesbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-%{version}
%{_datadir}/pixmaps/*.png
%if %{mdvver} < 201200
%{_datadir}/omf/*
%endif



%changelog
* Thu Mar 29 2012 Andrey Bondrov <abondrov@mandriva.org> 0.16.1-1mdv2011.0
+ Revision: 788219
- New version 0.16.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16.0-6mdv2011.0
+ Revision: 610984
- rebuild

* Wed Dec 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.16.0-5mdv2010.1
+ Revision: 479152
- fix build with gcc 4.3 (patch from Gentoo)
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Feb 08 2008 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2008.1
+ Revision: 164046
- drop old patch
- New version 0.16.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.15.0-1mdv2008.1
+ Revision: 131698
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import grhino


* Sat Jun 18 2005 Abel Cheung <deaddog@mandriva.org> 0.15.0-1mdk
- New release 0.15.0
- Supports GTP now (since 0.14)

* Sun Mar 27 2005 Abel Cheung <deaddog@mandrake.org> 0.13.0-1mdk
- New release 0.13.0
- Redo P0

* Mon Nov 29 2004 Abel Cheung <deaddog@mandrake.org> 0.12.0-2mdk
- Likely Rafael and me submitted same package at same time, so
  rebuild and pray for everything to automatically clean up themselves
  (Rafael, if you really did submit grhino, can you add your changes here?)

* Mon Nov 22 2004 Abel Cheung <deaddog@mandrake.org> 0.12.0-1mdk
- First Mandrake package
