%define version 0.16.0
%define release %mkrel 5

Summary:	An Othello/Reversi chess with strong AI
Name:		grhino
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Boards
URL:		http://rhino.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		grhino-0.16.0-gcc43.patch
Patch1:		grhino-0.16.0-mdv-fix-str-fmt.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeui2-devel
BuildRequires:	scrollkeeper
Requires(post,postun):		scrollkeeper

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
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name} 
Icon=%name 
Comment=Othello/Reversi chess with strong AI 
Categories=BoardGame;Game;GTK;GNOME; 
Name=GRhino
EOF

%find_lang %{name} --with-gnome --all-name

%if %mdkversion < 200900
%post
%update_menus
%update_scrollkeeper
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_scrollkeeper
%endif

%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%{name}-%{version}
%{_datadir}/pixmaps/*.png
%{_datadir}/omf/*
