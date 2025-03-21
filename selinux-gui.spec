%define	selinux_ver	3.8
Summary:	SELinux policy core utilities
Summary(pl.UTF-8):	Podstawowe narzędzia dla polityki SELinux
Name:		selinux-gui
Version:	3.8.1
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	16af5f4b3b8053ac610a7b2a7bd7fc77
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.507
BuildArch:	noarch
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
Requires:	gtk+3 >= 3
Requires:	policycoreutils >= %{selinux_ver}
Requires:	polkit
Requires:	python3-pygobject3 >= 3
Requires:	python3-selinux >= %{selinux_ver}
# seobject, sepolicy python modules
Requires:	python3-sepolicy >= %{selinux_ver}
# semanage and sepolicy commands
Requires:	selinux-python >= %{selinux_ver}

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

%py3_comp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n system-config-selinux -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/selinux-polgengui
%attr(755,root,root) %{_bindir}/system-config-selinux
%attr(755,root,root) %{_datadir}/system-config-selinux/system-config-selinux.py
%{_datadir}/system-config-selinux/[!ps]*.py
%{_datadir}/system-config-selinux/polgen.ui
%{_datadir}/system-config-selinux/portsPage.py
%{_datadir}/system-config-selinux/semanagePage.py
%{_datadir}/system-config-selinux/statusPage.py
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/system-config-selinux/system-config-selinux.ui
%{_datadir}/system-config-selinux/__pycache__
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_desktopdir}/selinux-polgengui.desktop
%{_desktopdir}/sepolicy.desktop
%{_desktopdir}/system-config-selinux.desktop
%{_iconsdir}/hicolor/*x*/apps/sepolicy.png
%{_iconsdir}/hicolor/24x24/apps/system-config-selinux.png
%{_pixmapsdir}/sepolicy.png
%{_pixmapsdir}/system-config-selinux.png
%{_mandir}/man8/selinux-polgengui.8*
%{_mandir}/man8/system-config-selinux.8*
