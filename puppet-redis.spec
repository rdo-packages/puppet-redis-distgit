Name:           puppet-redis
Version:        XXX
Release:        XXX
Summary:        Redis module
License:        Apache-2.0

URL:            http://arioch.github.io/puppet-redis/

Source0:        https://github.com/arioch/puppet-redis/archive/%{version}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-stdlib
Requires:       puppet-epel
Requires:       puppet >= 2.7.0

%description
Redis module

%prep
%setup -q -n %{name}-%{version}

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

