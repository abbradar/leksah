%global pkg_name regex-tdfa

%global common_summary Haskell %{pkg_name} library

%global common_description A new all Haskell "tagged" DFA regex engine, inspired by libtre.

%global ghc_pkg_deps ghc-regex-base-devel,ghc-parsec-devel,ghc-mtl-devel

%bcond_without shared

# debuginfo is not useful for ghc
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        1.1.2
Release:        1%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        BSD
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-rpm-macros >= 0.5.1
BuildRequires:  ghc-doc
BuildRequires:  ghc-prof
%{?ghc_pkg_deps:BuildRequires:  %{ghc_pkg_deps}, %(echo %{ghc_pkg_deps} | sed -e "s/\(ghc-[^, ]\+\)-devel/\1-doc,\1-prof/g")}
%{?ghc_pkg_c_deps:BuildRequires:  %{ghc_pkg_c_deps}}

%description
%{common_description}
%if %{with shared}
This package provides the shared library.
%endif


%{?ghc_lib_package}


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%cabal_configure --ghc -p
%cabal build
%cabal haddock


%install
rm -rf $RPM_BUILD_ROOT
%cabal_install
%cabal_pkg_conf

%ghc_gen_filelists


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue May 25 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.1.2-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.3
