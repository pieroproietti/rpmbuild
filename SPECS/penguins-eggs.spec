%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}


Name:           penguins-eggs
Version:        10.0.38
Release:        1%{?dist}
Summary:        A console tool that allows you to remaster your system and redistribute it as live image

License:        MIT
URL:            https://github.com/pieroproietti/penguins-eggs
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pnpm
Requires: bash-completion biosdevname cifs-utils cryptsetup curl device-mapper dmraid dosfstools dracut dracut-live fuse git iproute iscsi-initiator-utils jq lsb-release lvm2 mdadm nbd net-tools nfs-utils nodejs nvme-cli overlayfs-tools parted rng-tools rpcbind rpcbind  rsync squashfs-tools sshfs syslinux wicked xdg-user-dirs xorriso zstd

%description
.

%prep
%setup -q

%build
pnpm install
pnpm build

%install
mkdir -p %{buildroot}/%{_prefix}/lib/%{name}
cp -r ./* %{buildroot}/%{_prefix}/lib/%{name}
# crea link a run.js
mkdir -p %{buildroot}/%{_prefix}/bin
#ln -s %{buildroot}/%{_prefix}/lib/%{name}/bin/run.js %{buildroot}/%{_prefix}/bin/eggs

%files
# Elenca i file e le directory da includere nell'RPM
/usr/lib/penguins-eggs/

%changelog
* 14 09 2024 Piero Proietti <piero.proietti@gmail.com> - 10.0.38
- Prima versione del pacchetto penguins-eggs-10.0.38 per Fedora

