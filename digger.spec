Summary:	The Unix version of the old classic game Digger
Name:		digger
Version:	20121207
Release:	1
License:	GPLv2
Group:		Games/Arcade
Url:		http://www.digger.org/
# created from my branch at https://gitorious.org/digger with:
# git archive --prefix=digger-$(date +%Y%m%d)/ -o digger-$(date +%Y%m%d).tar --format tar HEAD
Source0:	%{name}-%{version}.tar.xz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
BuildRequires:	cmake
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

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

%build
%cmake
%make

%install
install -m755 build/digger -D %{buildroot}%{_gamesbindir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Digger Remastered
Comment=%{summary}
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

%files
%doc %{name}.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

