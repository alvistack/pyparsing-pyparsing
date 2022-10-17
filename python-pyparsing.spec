# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pyparsing
Epoch: 100
Version: 3.0.7
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package with an object-oriented approach to text processing
License: MIT
URL: https://github.com/pyparsing/pyparsing/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pyparsing is a module that can be used to easily and directly configure
syntax definitions for any number of text parsing applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pyparsing
Summary: Python package with an object-oriented approach to text processing
Requires: python3
Requires: python3-Jinja2
Requires: python3-railroad-diagrams
Provides: python3-pyparsing = %{epoch}:%{version}-%{release}
Provides: python3dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyparsing) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyparsing
pyparsing is a module that can be used to easily and directly configure
syntax definitions for any number of text parsing applications.

%files -n python%{python3_version_nodots}-pyparsing
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pyparsing
Summary: Python package with an object-oriented approach to text processing
Requires: python3
Requires: python3-Jinja2
Requires: python3-railroad-diagrams
Provides: python3-pyparsing = %{epoch}:%{version}-%{release}
Provides: python3dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyparsing) = %{epoch}:%{version}-%{release}

%description -n python3-pyparsing
pyparsing is a module that can be used to easily and directly configure
syntax definitions for any number of text parsing applications.

%files -n python3-pyparsing
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pyparsing
Summary: Python package with an object-oriented approach to text processing
Requires: python3
Requires: python3-jinja2
Requires: python3-railroad-diagrams
Provides: python3-pyparsing = %{epoch}:%{version}-%{release}
Provides: python3dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyparsing) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyparsing = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyparsing) = %{epoch}:%{version}-%{release}

%description -n python3-pyparsing
pyparsing is a module that can be used to easily and directly configure
syntax definitions for any number of text parsing applications.

%files -n python3-pyparsing
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
