%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-redis
%global commit 9711564ca49494d0eb1919e8c5668f68a50efa7d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-redis
Version:        1.2.3
Release:        2%{?alphatag}%{?dist}
Summary:        Redis module
License:        Apache-2.0

URL:            http://arioch.github.io/puppet-redis/

Source0:        https://github.com/arioch/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Redis module

%prep
%setup -q -n %{name}-%{upstream_version}

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.2.3-2.9711564.git
- Newton update 1.2.3 (9711564ca49494d0eb1919e8c5668f68a50efa7d)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.2.3-1
- Newton update 1.2.3 (6abc4f4ffbe718ed964a9672b3e75f3a88fc916d)


