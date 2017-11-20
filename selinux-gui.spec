Summary:	SELinux policy core utilities
Summary(pl.UTF-8):	Podstawowe narzędzia dla polityki SELinux
Name:		selinux-gui
Version:	2.7
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20170804/%{name}-%{version}.tar.gz
# Source0-md5:	f3555cb50a9e67b42bc917ede1982c7d
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

system-config-selinux provides a graphical interface for managing the
SELinux configuration.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

system-config-selinux dostarcza graficzny interfejs do zarządzania
konfiguracją SELinuksa.

%package -n system-config-selinux
Summary:	Graphical SELinux Management tool
Summary(pl.UTF-8):	Graficzne narzędzie do zarządzania SELinuksem
Group:		X11/Applications
Requires:	policycoreutils >= 2.7
Requires:	python-gnome >= 2
Requires:	python-pygobject >= 2
Requires:	python-pygtk-glade >= 2:2
Requires:	python-pygtk-gtk >= 2:2
Requires:	python-selinux
Requires:	python-sepolicy >= 2.7
Requires:	polkit
# semanage and sepolicy commands
Requires:	selinux-python >= 2.7

%description -n system-config-selinux
system-config-selinux provides a graphical interface for managing the
SELinux configuration.

%description -n system-config-selinux -l pl.UTF-8
system-config-selinux dostarcza graficzny interfejs do zarządzania
konfiguracją SELinuksa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux

%clean
rm -rf $RPM_BUILD_ROOT

%files -n system-config-selinux
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/system-config-selinux
%attr(755,root,root) %{_datadir}/system-config-selinux/polgengui.py
%attr(755,root,root) %{_datadir}/system-config-selinux/system-config-selinux.py
%{_datadir}/system-config-selinux/[!ps]*.py
%{_datadir}/system-config-selinux/portsPage.py
%{_datadir}/system-config-selinux/semanagePage.py
%{_datadir}/system-config-selinux/statusPage.py
%{_datadir}/system-config-selinux/*.py[co]
%{_datadir}/system-config-selinux/polgen.glade
%{_datadir}/system-config-selinux/selinux-polgengui.desktop
%{_datadir}/system-config-selinux/sepolicy.desktop
%{_datadir}/system-config-selinux/system-config-selinux.desktop
%{_datadir}/system-config-selinux/system-config-selinux.glade
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_iconsdir}/hicolor/*x*/apps/sepolicy.png
%{_iconsdir}/hicolor/24x24/apps/system-config-selinux.png
%{_pixmapsdir}/sepolicy.png
%{_pixmapsdir}/system-config-selinux.png
%{_mandir}/man8/selinux-polgengui.8*
%{_mandir}/man8/system-config-selinux.8*
