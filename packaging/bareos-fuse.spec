Name:           bareos-fuse
Version:        0.1
Release:        1%{?dist}
Summary:        Backup Archiving REcovery Open Sourced - FUSE
Group:          Productivity/Archiving/Backup
License:        AGPL-3.0
URL:            https://github.com/bareos/bareos-fuse/
Vendor:         The Bareos Team
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-root
BuildArch:      noarch
BuildRequires:  rsync
# for directory /etc/bareos/bareos-dir.d/
BuildRequires:  bareos-common
# required for restoring.
# Recommends would be enough, but not supported by all distributions.
Requires:       bareos-filedaemon >= 15.2.1
# fusermount
Requires:       fuse
Requires:       python-fuse
Requires:       python-bareos

%description
Bareos - Backup Archiving Recovery Open Sourced - FUSE

bareos-fuse allows you to display the information of a Bareos Backup System in your filesystem.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/bin %{buildroot}/etc  %{buildroot}/sbin
rsync -av bin/.  %{buildroot}/bin/.
rsync -av etc/.  %{buildroot}/etc/.
rsync -av sbin/. %{buildroot}/sbin/.


%check

%files
%defattr(-,root,root,-)
%doc README.md
%config(noreplace) %attr(644,root,root) /etc/bareos/bareos-dir.d/console/bareosfs.conf.example
%config(noreplace) %attr(644,root,root) /etc/bareos/bareos-dir.d/profile/bareosfs-all.conf
/bin/*
/sbin/*

%changelog
