Name:		python-rax-scheduled-images-python-novaclient-ext
Version:	0.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/rax-scheduled-images-python-novaclient-ext/rax_scheduled_images_python_novaclient_ext-%{version}.tar.gz
Summary:	Extends python-novaclient to use RAX-SI, the Rackspace Nova API Scheduled Images extension
URL:		https://pypi.org/project/rax-scheduled-images-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Extends python-novaclient to use RAX-SI, the Rackspace Nova API Scheduled Images extension

%files
%{py_sitedir}/rax_scheduled_images_python_novaclient_ext
%{py_sitedir}/rax_scheduled_images_python_novaclient_ext-*.*-info
