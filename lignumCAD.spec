Summary:	lignumCAD :  A Computer-Aided Design program for designing furniture
Summary(pl):	lignumCAD
Name:		lignumCAD
Version:	0.2
Release:	0.1
Copyright:	GPL/LGPL
Group:		X11/CAD
Source0:	%{name}.tar.gz
BuildRequires:	qt-devel >= 3.0.6
#BuildRequires:	OpenCASCADE-devel >= 4
#BuildRequires:	freetype-devel >= 2.1.3
#BuildRequires:	OpenGL-devel >= 4.1
#Requires:
URL: http://www.lignumcomputing.com/lignumcad/
#URL:		http://lignumcad.sourceforge.net
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
lignumCAD is a Computer-Aided Design (CAD) program geared specifically
to aid the woodworker in designing custom furniture and other hand-made
objects. It supports both two-dimensional and three-dimensional
representations of the design with full parametric interrelations.
Additional features include optimized layout of the bill of materials
on custom stock and photo-realistic rendering of the final design.

%description -l pl

%prep
%setup -q -n %{name}

#%patch

%build
qmake lignumCAD.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%postun


%files
%defattr(644,root,root,755)
%doc
%dir /opt/lignumCAD/
%dir /opt/lignumCAD/v%{version}
%dir /opt/lignumCAD/v%{version}/bin
%dir /opt/lignumCAD/v%{version}/doc
%dir /opt/lignumCAD/v%{version}/translations
%dir /opt/lignumCAD/v%{version}/materials
/opt/lignumCAD/v%{version}/bin/lignumCAD
%docdir /opt/lignumCAD/v%{version}/doc
/opt/lignumCAD/v%{version}/doc
/opt/lignumCAD/v%{version}/translations
/opt/lignumCAD/v%{version}/materials
