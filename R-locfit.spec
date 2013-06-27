%global packname  locfit
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          19980714.2
Release:          1
Summary:          Local Regression, Likelihood and Density Estimation
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/locfit/locfit_19980714-2.tar.gz
Requires:         R-akima R-lattice 
Requires:         R-gam 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-akima R-lattice
BuildRequires:    R-gam 

%description
Local regression, likelihood and density estimation.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5_6-2
+ Revision: 776583
- Rebuild.
- Import R-locfit
- Import R-locfit


