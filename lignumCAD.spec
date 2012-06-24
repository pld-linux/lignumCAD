Summary:	lignumCAD - A Computer-Aided Design program for designing furniture
Summary(pl):	lignumCAD - program do komputerowo wspomaganego projektowania mebli
Name:		lignumCAD
Version:	0.2
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications/Science
Source0:	%{name}.tar.gz
Patch0:		%{name}-gcc3.patch
BuildRequires:	qt-devel >= 3.0.6
#BuildRequires:	OpenCASCADE-devel >= 4
#BuildRequires:	OpenGL-devel >= 4.1
#BuildRequires:	freetype-devel >= 2.1.3
URL:		http://www.lignumcomputing.com/lignumcad/
#URL:		http://lignumcad.sourceforge.net
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lignumCAD is a Computer-Aided Design (CAD) program geared specifically
to aid the woodworker in designing custom furniture and other hand-made
objects. It supports both two-dimensional and three-dimensional
representations of the design with full parametric interrelations.
Additional features include optimized layout of the bill of materials
on custom stock and photo-realistic rendering of the final design.

%description -l pl
lignumCAD jest programem komputerowego wspierania projektowania (CAD)
stworzonym specjalnie dla stolarzy, aby u�atwi� tworzenie
indywidualnych projekt�w mebli i innych recznie wykonywanych
przedmiot�w. Wspiera on zar�wno dwu- jak i tr�jwymiarowe prezentacje
projektu z pe�n� parametryzacj� wzajemnych zale�no�ci. Dodatkowe
mozliwo�ci programu obejmuj� zoptymalizowane przedstawienie
rozliczenia materia��w oraz fotagraficznie realistyczne symulacja
ko�cowego wygl�du przedmiotu projektu.

%prep
%setup -q -n %{name}
# only partial (to the point where OpenCascade is required), needs finishing
%patch -p1

%build
export QTDIR=/usr
qmake lignumCAD.pro
%{__make} \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -W -D_REENTRANT  -DOGLFT_NO_SOLID -DGL2PS_USE_QT -DGL2PS_USE_EMF -DQT_THREAD_SUPPORT -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%dir /opt/lignumCAD
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
