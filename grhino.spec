%define version 0.15.0
%define release %mkrel 1

Summary:	An Othello/Reversi chess with strong AI
Name:		grhino
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://rhino.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		grhino-0.13.0-destdir.patch.bz2
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
%patch0 -p1 -b .destdir

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
Icon=strategy_section 
Comment=Othello/Reversi chess with strong AI 
Categories=BoardGame; 
Name=GRhino
EOF

# move omf file to correct location
mkdir -p %{buildroot}%{_datadir}/omf/%{name}
mv %{buildroot}%{_datadir}/gnome/help/%{name}/C/*.omf %{buildroot}%{_datadir}/omf/%{name}/

%find_lang %{name} --with-gnome --all-name


%post
%update_menus
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q; fi

%postun
%clean_menus
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q; fi

%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_gamesbindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%{name}-%{version}
%{_datadir}/omf/*

