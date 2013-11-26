%define		fversion	%(echo %{version} |tr r -)
%define		modulename	abind
Summary:	Combine multi-dimensional arrays
Summary(pl.UTF-8):	Łączenie wielowymiarowych tablic
Name:		R-cran-%{modulename}
Version:	1.4r0
Release:	2
License:	LGPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	4dd1b633959a2fc73491e897f84857a7
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Combine multi-dimensional arrays. This is a generalization of cbind
and rbind. Takes a sequence of vectors, matrices, or arrays and
produces a single array of the same or higher dimension.

%description -l pl.UTF-8
Moduł ten łączy wielowymiarowe tablice. Jest uogólnieniem cbind i
rbind. Pobiera listę wektorów, macierzy lub tablic i tworzy pojedynczą
tablice tego samego lub wyższego wymiaru.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,ChangeLog}
%{_libdir}/R/library/%{modulename}
