Summary:	lignumCAD - A Computer-Aided Design program for designing furniture
Summary(pl.UTF-8):	lignumCAD - program do komputerowo wspomaganego projektowania mebli
Name:		lignumCAD
Version:	0.2
Release:	1
License:	GPL/LGPL
Group:		X11/Applications/Science
Source0:	%{name}.tar.gz
Patch0:		%{name}-gcc3.patch
Patch1:		%{name}-gcc34.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-gcc41.patch
Patch4:		%{name}-gcc42.patch
Patch5:		%{name}-gcc43.patch
Patch6:		%{name}-gcc44.patch
Patch7:		%{name}-gcc-enum-warning.patch
Patch8:		%{name}-delete-pointer.patch
Patch9:		%{name}-ui.patch
Patch10:	%{name}-xft.patch
Patch11:	%{name}-Xft.patch
Patch12:	%{name}-qt3.patch
URL:		http://lignumcad.sourceforge.net/
BuildRequires:	OpenCASCADE-devel >= 4
BuildRequires:	OpenGL-GLU-devel >= 1.3
BuildRequires:	freetype-devel >= 2.1.3
BuildRequires:	libEMF-devel
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3:3.0.6
BuildRequires:	sed >= 4.0
Requires:	fonts-TTF-DejaVu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lignumCAD is a Computer-Aided Design (CAD) program geared specifically
to aid the woodworker in designing custom furniture and other hand-made
objects. It supports both two-dimensional and three-dimensional
representations of the design with full parametric interrelations.
Additional features include optimized layout of the bill of materials
on custom stock and photo-realistic rendering of the final design.

%description -l pl.UTF-8
lignumCAD jest programem komputerowego wspierania projektowania (CAD)
stworzonym specjalnie dla stolarzy, aby ułatwić tworzenie
indywidualnych projektów mebli i innych ręcznie wykonywanych
przedmiotów. Wspiera on zarówno dwu- jak i trójwymiarowe prezentacje
projektu z pełną parametryzacją wzajemnych zależności. Dodatkowe
możliwości programu obejmują zoptymalizowane przedstawienie
rozliczenia materiałów oraz fotograficznie realistyczne symulacje
końcowego wyglądu przedmiotu projektu.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0
sed -i -e "s|/opt/lignumCAD|%{_datadir}/%{name}|" configuration.h
sed -i -e 's/\(lib\)*emf.\(h\|cpp\)//g' lignumCAD.pro
sed -i -e 's/DELETE /LDELETE/' constants.h command.cpp
%{__rm} *emf.{h,cpp}

%build
export QTDIR=/usr
qmake lignumCAD.pro \
	unix:LIBS="-lGL -lTKTopAlgo -lTKGeomAlgo -lTKBRep -lTKGeomBase -lTKG3d -lTKG2d -lTKMath -lTKernel -lfontconfig -lTKMesh -lTKBool -lTKBO -lTKPrim -lEMF" \
	-after \
	unix:INCLUDEPATH+=%{_includedir}/{OpenCASCADE,X11/Xft,freetype2,libEMF} \
	en_documentation.files='' \
	en_documentation_graphics.files='' \
	en_so_documentation.files='' \
	en_so_documentation_graphics.files='' \
	de_documentation_graphics.files='' \
	de_so_documentation.files='' \
	translations.path=%{_datadir}/%{name}/v%{version}/translations \
	materials.path=%{_datadir}/%{name}/v%{version}/material \
	material_images.path=%{_datadir}/%{name}/v%{version}/material/images \
	target.path=%{_bindir}

%{__make} \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -W -D_REENTRANT -DOGLFT_NO_SOLID -DGL2PS_USE_QT -DGL2PS_USE_EMF -DQT_THREAD_SUPPORT"

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=/usr
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/v%{version}/material{,s}
%{__ln_s} %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/v%{version}/doc
%{__ln_s} %{name}_en.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/v%{version}/translations/%{name}_C.qm
%{__ln_s} %{name}_C.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/v%{version}/translations/qt_C.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/v%{version}
%{_datadir}/%{name}/v%{version}/doc
%{_datadir}/%{name}/v%{version}/materials
%dir %{_datadir}/%{name}/v%{version}/translations
%lang(de) %{_datadir}/%{name}/v%{version}/translations/*_de.qm
%{_datadir}/%{name}/v%{version}/translations/%{name}_en.qm
%{_datadir}/%{name}/v%{version}/translations/*_C.qm
