Summary:	lignumCAD
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
URL:		http://lignumcad.sourceforge.net
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%prep
%setup -q -n %{name}

#%patch

%build
qmake lignumCAD

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
