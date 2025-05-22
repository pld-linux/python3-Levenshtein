#
# Conditional build:
%define 	module		Levenshtein
%define 	egg_name	levenshtein
%define		pypi_name	python-Levenshtein
Summary:	Python extension computing string distances and similarities
Summary(pl.UTF-8):	Rozszerzenie Pythona do obliczania odległości i podobieństw łańcuchów
Name:		python3-%{module}
Version:	0.27.1
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	https://pypi.debian.net/Levenshtein/levenshtein-%{version}.tar.gz
# Source0-md5:	3f10add315701638918d8039ff8dfe44
URL:		https://github.com/rapidfuzz/Levenshtein
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:2.3.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Levenshtein computes Levenshtein distances, similarity ratios,
generalized medians and set medians of Strings and Unicodes. Becuase
it's implemented in C, it's much faster than corresponding Python
library functions and methods.

%description -l pl.UTF-8
Levenshtein oblicza odległości Levenshteina, współczynniki
podobieństwa, uogólnione mediany i mediany zbiorów dla wartości String
i Unicode. Ponieważ jest zaimplementowany w C, jest dużo szybszy od
odpowiadających mu funkcji bibliotecznych i metod Pythona.

%prep
%setup -q -n levenshtein-%{version}

%build
export SKBUILD_CMAKE_BUILD_TYPE=RelWithDebInfo
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md HISTORY.md SECURITY.md
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/*.pyi
%{py3_sitedir}/%{module}/py.typed
%dir %{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/__pycache__/*.py[co]
%attr(755,root,root) %{py3_sitedir}/%{module}/levenshtein*.cpython*.so
%{py3_sitedir}/%{egg_name}-%{version}.dist-info
