%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-redis
%global commit d44386133a7c524ba0f31d375cf91533f78db1cc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-redis
Version:        6.1.1
Release:        0.1%{?milestone}%{?alphatag}%{?dist}
Summary:        Redis module
License:        ASL 2.0

URL:            http://arioch.github.io/puppet-redis/

Source0:        https://github.com/arioch/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0
Requires:       puppet-systemd

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
* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 6.1.1-0.1.0rc0.d443861git
- Update to post 6.1.1-rc0 (d44386133a7c524ba0f31d375cf91533f78db1cc)


