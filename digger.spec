Name:		digger
Version:	20121207
Release:	1
# created from my branch at https://gitorious.org/digger with:
# git archive --prefix=digger-$(date +%Y%m%d)/ -o digger-$(date +%Y%m%d).tar --format tar HEAD
Source0:	%{name}-%{version}.tar.xz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPLv2
Group:		Games/Arcade
URL:		http://www.digger.org/
Summary:	The Unix version of the old classic game Digger
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake

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
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%changelog
* Thu Jan 26 2012 Andrey Bondrov <abondrov@mandriva.org> 20110916-1
+ Revision: 769133
- Update version to 20110916 (latest git snapshot at this moment)

  + Per Ã˜yvind Karlsen <peroyvind@mandriva.org>
    - update to newer version created from my own branch:
      	o fixes alsa buffer underrun
      	o readdir() symbol crash causing segfault with pulseaudio
      	o misc cleanups & fixes of code
    - clean out old rpm junk

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 20020314-9mdv2011.0
+ Revision: 610243
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 20020314-8mdv2010.1
+ Revision: 508124
- BR zlib

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 20020314-6mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 09 2007 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 20020314-6mdv2007.1
+ Revision: 138906
- Import digger

* Fri Mar 09 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 20020314-6mdv2007.1
- digger is now truly free, import to contrib
- update digger.txt accordingly (P2)
- cleanups
- xdg menu
- disable sound as it's broken (TODO: fix this!)

* Wed Apr 27 2005 Nicolas Lécureuil <neoclust@zarb.org> 20020314-5plf
- Birthday rebuild

