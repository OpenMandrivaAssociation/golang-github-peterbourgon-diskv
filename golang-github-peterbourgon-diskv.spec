# Run tests in check section
%bcond_without check

# https://github.com/peterbourgon/diskv
%global goipath         github.com/peterbourgon/diskv
Version:                2.0.1

%global common_description %{expand:
Diskv (disk-vee) is a simple, persistent key-value store written in the Go 
language. It starts with an incredibly simple API for storing arbitrary data 
on a filesystem by key, and builds several layers of performance-enhancing 
abstraction on top. The end result is a conceptually simple, but highly 
performant, disk-backed storage system.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        A disk-backed key-value store
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

# Fixed in https://github.com/peterbourgon/diskv/commit/d36d2a24e0a5ef9fcb823c861cba040ecaeda71d
# Delete in next release
Patch0:         diskv-2.0.1-fix_printf.patch

BuildRequires: golang(github.com/google/btree)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- First package for Fedora

