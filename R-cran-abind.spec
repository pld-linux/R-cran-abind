%define		fversion	%(echo %{version} |tr r -)
%define		modulename	abind
Summary:	Combine multi-dimensional arrays
Summary(pl):	£±czy wielowymiarowe tablice
Name:		R-cran-%{modulename}
Version:	1.1r0
Release:	1
License:	LGPL Version 2 or later.
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	e70921be502d58d9edb1a1b64af44d48
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Combine multi-dimensional arrays. This is a generalization of cbind
and rbind. Takes a sequence of vectors, matrices, or arrays and
produces a single array of the same or higher dimension.

%description -l pl
£±czy wielowymiarowe tablice. Jest uogólnieniem cbind i rbind. Pobiera listê
wektorów, matryc lub tablic oraz tworzy pojedyñcz± tablice tego samego lub
wy¿szego wymiaru.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,ChangeLog}
%{_libdir}/R/library/%{modulename}
