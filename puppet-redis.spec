%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-redis
%global commit 989403c3b291ec3d529490076bcc4772af3c11a0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-redis
Version:        3.3.0
Release:        1%{?alphatag}%{?dist}
Summary:        Redis module
License:        ASL 2.0

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 3.3.0-1.989403cgit
- Update to post 3.3.0 (989403c3b291ec3d529490076bcc4772af3c11a0)



