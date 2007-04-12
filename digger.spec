%define name	digger
%define version	20020314
%define release %mkrel 6
%define Summary The Unix version of the old classic game Digger

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		digger-optflags.patch
Patch1:		digger-fix_gcc_3.patch
Patch2:		digger-20020314-update-digger.txt-with-legal-info.patch
License:	GPL
Group:		Games/Arcade
URL:		http://www.digger.org/
Summary:	%{Summary}
BuildRequires:	SDL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the Unix version of the old classic game Digger.
It has many new features including:
* Exit button
* Optional VGA graphics
* Recording and playback
* Real time speed control
* Keyboard redefinition
* Gauntlet mode
* Two player simultaneous mode

%prep
%setup -q
%patch0 -p0 -b .optflags
%patch1 -p0 -b .gcc3
%patch2 -p1 -b .legal

%build
%make -f Makefile.sdl OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -m755 digger -D %{buildroot}%{_gamesbindir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Digger Remastered
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{name}.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


