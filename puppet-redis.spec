%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-redis

Name:           puppet-redis
Version:        XXX
Release:        XXX
Summary:        Redis module
License:        ASL 2.0

URL:            http://arioch.github.io/puppet-redis/

Source0:        https://github.com/arioch/%{upstream_name}/archive/v%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0
Requires:       puppet-systemd

%description
Redis module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/redis/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/redis/



%files
%{_datadir}/openstack-puppet/modules/redis/


%changelog


