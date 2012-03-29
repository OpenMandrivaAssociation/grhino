Name:		grhino
Version:	0.16.1
Release:	%mkrel 1
Summary:	An Othello/Reversi chess with strong AI
License:	GPLv2+
Group:		Games/Boards
URL:		http://rhino.sourceforge.net/
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

