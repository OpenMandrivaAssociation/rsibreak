Name:		rsibreak
Version:	0.12
Summary:	Assists in the Recovery and Prevention of Repetitive Strain Injury
Release:	1
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://www.rsibreak.org
Source0:	http://www.rsibreak.org/files/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5WindowSystem)

%description
Repetitive Strain Injury is an illness which can occur as a result of
working with a mouse and keyboard. This utility can be used to remind
you to take a break now and then.

%files  -f %{name}.lang
%defattr(-,root,root)
%{_kde5_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/rsibreak_autostart.desktop
%{_kde5_datadir}/applications/rsibreak.desktop
%{_kde5_iconsdir}/hicolor/*/*/*
%{_kde5_datadir}/dbus-1/interfaces/org.rsibreak.rsiwidget.xml
%{_kde5_datadir}/knotifications5/rsibreak.notifyrc
%{_kde5_docdir}/HTML/*/rsibreak

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

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


