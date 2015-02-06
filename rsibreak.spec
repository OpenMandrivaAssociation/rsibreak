Name:		rsibreak
Version:	0.11
Summary:	Assists in the Recovery and Prevention of Repetitive Strain Injury
Release:	2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.rsibreak.org
Source0:	http://www.rsibreak.org/files/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime

%description
Repetitive Strain Injury is an illness which can occur as a result of
working with a mouse and keyboard. This utility can be used to remind
you to take a break now and then.

%files  -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_appsdir}/rsibreak/rsibreak.notifyrc
%{_kde_datadir}/autostart/rsibreak.desktop
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_datadir}/applications/kde4/rsibreak.desktop
%{_kde_datadir}/dbus-1/interfaces/org.rsibreak.rsiwidget.xml
%{_kde_docdir}/HTML/*/rsibreak

#-----------------------------------------------------------------------------

%package -n plasma-applet-rsibreak
Summary:	Plasma applet for rsibreak
Group:		Graphical desktop/KDE
Requires:	%{name} = %{version}
Requires:	plasma-engine-rsibreak = %{version}
Provides:	plasma-applet
Conflicts:	extragear-plasma < 4.0.82
Conflicts:	kdebase4-workspace < 2:4.1.80-6

%description -n plasma-applet-rsibreak
Plasma applet for rsibreak

%files -n plasma-applet-rsibreak -f plasma_applet_rsibreak.lang
%defattr(-,root,root)
%{_kde_services}/plasma-applet-rsibreak.desktop
%{_kde_libdir}/kde4/plasma_applet_rsibreak.so
%{_kde_appsdir}/desktoptheme/default/widgets/rsibreak.svg

#--------------------------------------------------------------------

%package -n plasma-engine-rsibreak
Summary:	Plasma engine for rsibreak
Group:		Graphical desktop/KDE
Provides:	plasma-engine

%description -n plasma-engine-rsibreak
Plasma engine for rsibreak

%files -n plasma-engine-rsibreak
%defattr(-,root,root)
%{_kde_services}/plasma-engine-rsibreak.desktop
%{_kde_libdir}/kde4/plasma_engine_rsibreak.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name}
%find_lang plasma_applet_rsibreak

%clean
%__rm -rf %{buildroot}



%changelog
* Wed Feb 01 2012 Andrey Bondrov <abondrov@mandriva.org> 0.11-1
+ Revision: 770416
- New version 0.11

  + John Balcaen <mikala@mandriva.org>
    - Fix applet category
    - clean spec

* Sun Jul 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10-1mdv2010.0
+ Revision: 397929
- Update to new version 0.10
- Remove cmake patch which is not needed anymore

* Sun Mar 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.0-3mdv2009.1
+ Revision: 355556
- Fix build  against new KDE4
- Rebuild against new KDE4

* Mon Dec 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.0-2mdv2009.1
+ Revision: 317691
- Rebuild against kde 4.1.85

* Fri Nov 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.0-1mdv2009.1
+ Revision: 307336
- import rsibreak


