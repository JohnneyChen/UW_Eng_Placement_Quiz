from .models import *


# saving all the engineering programs
ce = Program()
ce.key = 'ce'
ce.program_name = 'Computer Engineering'
ce.site = 'https://uwaterloo.ca/future-students/programs/computer-engineering'
ce.description = "“Why choose? Develop software savvy and hardware know-how.” Want to design a brain stimulator to combat symptoms of Parkinson's disease? Develop software to protect companies from cyber attacks? Create the next groundbreaking gaming platform? Learn at one of the top 50 universities in the world for Computer Engineering? (Shanghai World University Rankings 2020) Between labs and lectures, you'll gain experience with all aspects of computers, from chips and wiring to software, networks, and communications. Meanwhile, your co-op terms will give you 2 years of paid work experience. You’ll graduate ready for a career as a software developer, hardware engineer, IT specialist, systems designer, and more."
ce.save()

elec = Program()
elec.key = 'elec'
elec.program_name = 'Electrical Engineering'
elec.site = 'https://uwaterloo.ca/future-students/programs/electrical-engineering'
elec.description = "“Set yourself up for an electrifying future.” Behind just about every advance in information, power, and energy, you’ll find an electrical engineer. Join the ranks of those innovators with a degree from Waterloo, whose electrical engineering program is ranked in the top 75 internationally (Shanghai World University Rankings 2020). You’ll study the fundamentals of electromagnetism, circuits, algorithms, and instrumentation. You'll also gain hands-on experience starting right in first year, thanks to paid co-op work terms and some of the best electrical engineering student labs in North America. When you graduate, you’ll have hundreds of career paths open to you: from designing power stations and aircraft control systems to pioneering the future of microprocessors and telecommunications systems."
elec.save()

mech = Program()
mech.key = 'mech'
mech.program_name = 'Mechanical Engineering'
mech.site = 'https://uwaterloo.ca/future-students/programs/mechanical-engineering'
mech.description = "“Put your career in gear.” If you love things that move, this is your program. At Waterloo, you’ll develop the skills you need to design everything from switches to spacecraft. You’ll get a broad foundation in all aspects of mechanical design: mechanics, power, control, and manufacturing. You’ll also learn to lead large, multidisciplinary teams, solve problems, come up with high-impact innovations, and have the chance to apply it all to real work experiences in co-op. Where you use those skills is up to you. Mechanical engineers work in all kinds of fields, constantly looking for ways to make machinery faster, lighter, cleaner, and more reliable. And with two years of career-relevant experience on your résumé by the time you graduate, you’ll definitely impress potential employers."
mech.save()

bmed = Program()
bmed.key = 'bmed'
bmed.program_name = 'Biomedical Engineering'
bmed.site = 'https://uwaterloo.ca/future-students/programs/biomedical-engineering'
bmed.description = "“Improve the health of others (without the hefty med school bill).” Design bionic limbs. Create laser-guided surgical devices. Develop wearable tech to help athletes perform better. In Biomedical Engineering, you’ll use engineering know-how to develop better ways to diagnose illnesses, treat health problems, and enhance health. You’ll study biomechanics, physics, chemistry, and design. With that broad knowledge, you’ll be able to collaborate with all kinds of different experts: biologists, medical practitioners, policy makers, and engineers, to name a few. You’ll also learn to model and design complex biomedical systems—and you’ll get plenty of hands-on experience through two years of paid co-op work terms, plus a fourth-year design project. By the time you graduate, you’ll be ready to create tomorrow’s life-saving and life-enhancing innovations."
bmed.save()

syde = Program()
syde.key = 'syde'
syde.program_name = 'System Design Engineering'
syde.site = 'https://uwaterloo.ca/future-students/programs/systems-design-engineering'
syde.description = "“Get creative. And still get an engineering degree.” Cross boundaries. Connect the dots. Look at the bigger picture. Systems Design is designed for people who want the rigour of an engineering degree plus the flexibility to explore topics outside traditional engineering disciplines. You’ll examine the people, materials, tools, software, and other factors involved in any engineering problem. You’ll learn to look at the system as a whole and assess how one change will affect another element, using a variety of modelling, analysis, and design methods. Our project-based approach gives you lots of opportunities to apply your learning to real problems. Plus you’ll get two full years of work experience through our co-op program. Once you graduate, your options are wide open: our grads go on to engineering consulting, project management, graduate school, medical school, startups, and more."
syde.save()

geo = Program()
geo.key = 'geo'
geo.program_name = 'Geological Engineering'
geo.site = 'https://uwaterloo.ca/future-students/programs/geological-engineering'
geo.description = "“Put your future on solid ground - and help the world do the same.” Use your knowledge of soil and rock behaviour to solve complex problems. Ensure the safety of dams and pipelines, assess risks for landslides and earthquakes, remove hazardous waste from groundwater, and more. Waterloo’s program is one of only two in Ontario. You’ll take Civil Engineering classes, where you’ll learn design and problem-solving skills. You’ll also take Earth Sciences classes, where you’ll acquire a solid background in geosciences. Meanwhile, through co-op, you'll gain two full years of related work experience. When you graduate, your degree can take you around the world — working in oil and gas, mineral exploration, hazard waste removal, groundwater management, and more."
geo.save()

arch = Program()
arch.key = 'arch'
arch.program_name = 'School of Architechture'
arch.site = 'https://uwaterloo.ca/future-students/programs/architecture'
arch.description = "“Create the blueprints for a great career.” In one of North America’s top schools of architecture, you’ll get a broad education that covers everything from building materials and construction techniques to cultural history, social context, green architecture, and more. Not to mention you can combine it all with co-op. However, the core of pre-professional program is design courses, starting right in year one. You’ll get your own dedicated space in our studio where you’ll develop your ideas and skills through a series of hands-on projects. Learn about society and culture, the principles of physics, materials and techniques of construction, human interaction with the natural and built environment, critical thought, and the diverse forms of creative expression. It all happens in a beautiful historic building in the city of Cambridge, about 30 kilometres south of the main Waterloo campus, complete with labs, exhibition galleries, and a world-class design library."
arch.save()

arche = Program()
arche.key = 'arch-e'
arche.program_name = 'Architectural Engineering'
arche.site = 'https://uwaterloo.ca/future-students/programs/architectural-engineering'
arche.description = "“Build better buildings - and a brighter career in the process.” Combine engineering expertise with architectural savvy to boost the energy efficiency, durability, and sustainability of buildings. In Waterloo's newest engineering program, you'll learn how to design, renovate, and retrofit flexible buildings that adapt to different needs. And have the opportunity to combine it all with co-op. You'll cover all the science and engineering that goes into good building design, including mechanics, structural analysis, structural design and more. In third year, you'll study at Waterloo's world-class School of Architecture, deepening your understanding of aesthetics, culture, and other elements of design. As a result, you'll graduate speaking the language of both engineers and architects — a skill that will put you on the fast track to leadership in the building design industry."
arche.save()

env = Program()
env.key = 'env'
env.program_name = 'Environmental Engineering'
env.site = 'https://uwaterloo.ca/future-students/programs/environmental-engineering'
env.description = "“Save the environment. Get an engineering degree.” Clean up contaminated soil. Prevent E. coli outbreaks. Design smarter ways to treat and manage water. Canada’s largest Environmental Engineering program gives you the technical rigour of an engineering degree combined with scientific know-how and environmental insights. As it's also one of the top 100 environmental engineering programs in the world (Shanghai World University Rankings 2020), you’ll take courses in engineering, chemistry, biology, geology, and more, drawing on that broad base of knowledge to tackle water, soil, and air pollution. Meanwhile, you’ll gain two years of paid experience through your co-op work terms, allowing you to earn money to help pay for your education and discover the career areas that fit you best. You’ll graduate ready to clean up the world’s pollution — and to prevent future environmental problems."
env.save()

nano = Program()
nano.key = 'nano'
nano.program_name = 'Nanotechnology Engineering'
nano.site = 'https://uwaterloo.ca/future-students/programs/nanotechnology-engineering'
nano.description = "“Design solutions measured in billionths of a meter.” Nanotechnology is revolutionizing everything from smartphones to cancer treatment. Put yourself on the forefront of that revolution at Waterloo. In Canada’s only undergraduate nanotechnology engineering program, you’ll use principles from biology, chemistry, electronics, and quantum physics to create materials and machines far too small to see with the naked eye. You'll gain extensive experience in your lab courses and through co-op positions at places like Mercedes-Benz, Harvard Medical School, and MIT. In your upper years, you’ll spend eighth months at a time on work terms, so you can really dig deep into a project — and graduate with a seriously impressive résumé."
nano.save()

msci = Program()
msci.key = 'msci'
msci.program_name = 'Management Engineering'
msci.site = 'https://uwaterloo.ca/future-students/programs/management-engineering'
msci.description = "“Smooth moves: get a degree in making processes flow better.” Cut waiting times for surgery. Streamline supply chains. Fine-tune airline routes. In Canada’s first and only Management Engineering program, you’ll learn to analyze how organizations operate and apply engineering skills to increase their efficiency. Over the course of your degree, you’ll develop expertise in data analytics, information systems, operations and supply chain management, and organizational behaviour. You'll also have the opportunity to gain paid work experience through co-op. By graduation, you’ll have the know-how to design and manage complex systems, optimizing the flow of energy, materials, people, and information. And you’ll find no shortage of companies looking for your skills: in software, finance, supply chain management, health care, manufacturing, and more."
msci.save()

cive = Program()
cive.key = 'cive'
cive.program_name = 'Civil Engineering'
cive.site = 'https://uwaterloo.ca/future-students/programs/civil-engineering'
cive.description = "“Make the world your sandbox. (Hardhat included.)” Bring on the bulldozers! In one of Canada’s largest (and the world's top 100) civil engineering programs, you’ll learn to design and maintain the massive infrastructure we all depend on: bridges, highways, airports, tunnels, dams, pollution-control facilities, and more. This is a degree with lots of flexibility. Once you’ve completed your foundational courses, you can choose from a wide variety of technical electives in structural, transportation, geotechnical, and water/environmental engineering. You’ll apply your knowledge during your six co-op work terms. This is your chance to test drive different career options: work for major construction and engineering companies, get experience with local or provincial governments, or spend a term abroad. You’ll graduate ready to create structures — in Canada or overseas — that stand the test of time."
cive.save()

swe = Program()
swe.key = 'swe'
swe.program_name = 'Software Engineering'
swe.site = 'https://uwaterloo.ca/future-students/programs/software-engineering'
swe.description = "“Because today, even your fridge is full of software.” Whether you want to create a VR training program for surgeons, the next \"swipe right\" dating app, or an autonomous car, software engineers have endless career options in today’s tech-enabled world. At Waterloo, you won’t just write code. You’ll also analyze software architecture, apply algorithms, understand digital hardware systems, and design human/ computer interfaces. Plus, you’ll learn how to work in teams and manage projects, all while being taught by one of the best universities on the planet for software engineering (Shanghai World University Rankings 2020). Then, during your co-op, you’ll put those skills to work at leading companies like Snapchat or Facebook or hot new startups. When you graduate, you’ll be ready to create reliable, affordable, and faster software for all kinds of different purposes."
swe.save()

tron = Program()
tron.key = 'tron'
tron.program_name = 'Mechatronics Engineering'
tron.site = 'https://uwaterloo.ca/future-students/programs/mechatronics-engineering'
tron.description = "“Build the next generation of robots (and cars and wearable tech and…)” From the ATM down the street to the drone that will one day deliver your pizza, computer-controlled electromechanical systems drive all kinds of technology. Learn to design those systems in Waterloo’s Mechatronics Engineering program — the first of its kind in Canada and one of the top 100 in the world (Shanghai World University Rankings 2020). You’ll develop expertise in mechanical engineering, electronics, control engineering, and computer science, pulling together know-how from these different fields to develop sophisticated machines. During your co-op terms, you’ll have the chance to try out different career paths, earn money to pay for your education, and build a résumé guaranteed to impress potential employers."
tron.save()

chem = Program()
chem.key = 'chem'
chem.program_name = 'Chemical Engineering'
chem.site = 'https://uwaterloo.ca/future-students/programs/chemical-engineering'
chem.description = "“Put your creativity and problem solving to the test.” Learn to engineer the products we use every day. Turn fuel into energy, waste into resources, and raw material into finished products in one of the largest chemical engineering departments in Canada, and one of the top 100 in the world. You’ll develop expertise in chemistry and materials science — plus you’ll learn the systems analysis skills to design, implement, and manage processes from start to finish. You’ll put that knowledge to work during your six co-op terms: creating an impressive résumé, exploring different career areas, and earning money to help pay for your education."
chem.save()

# computer engineering first-year courses
ce.course_set.create(course_type='first', course='ECE 102 - Information Session')
ce.course_set.create(course_type='first', course='MATH 117 - Calculus 1 for Engineering')
ce.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
ce.course_set.create(course_type='first', course='ECE 190 - Engineering Profession and Practice')
ce.course_set.create(course_type='first', course='ECE 150 - Fundamentals of Programming')
ce.course_set.create(course_type='first', course='ECE 105 - Classical Mechanics')
ce.course_set.create(course_type='first', course='GENE 191 - Communication in the Engineering Profession')
ce.course_set.create(course_type='first', course='MATH 119 - Calculus 2 for Engineering')
ce.course_set.create(course_type='first', course='ECE 192 - Engineering Economics and Impact on Society')
ce.course_set.create(course_type='first', course='ECE 140 - Linear Circuits')
ce.course_set.create(course_type='first', course='ECE 124 - Digital Circuits and Systems')
ce.course_set.create(course_type='first', course='ECE 108 - Discrete Mathematics and Logic 1')
ce.course_set.create(course_type='first', course='ECE 106 - Electricity and Magnetism')

# computer engineering upper-year courses
ce.course_set.create(course_type='upper', course='ECE 452 – Software Design and Architectures')
ce.course_set.create(course_type='upper', course='ECE 405 – Introduction to Quantum Mechanics')
ce.course_set.create(course_type='upper', course='ECE 320 – Computer Architecture')
ce.course_set.create(course_type='upper', course='ECE 254 – Operating Systems and Systems Programming')

# computer engineering coop
ce.career_set.create(career_type="coop", career="QA developer")
ce.career_set.create(career_type="coop", career="Infrastructure engineering intern")
ce.career_set.create(career_type="coop", career="iOS developer")
ce.career_set.create(career_type="coop", career="Data scientist")
ce.career_set.create(career_type="coop", career="Data engineering student")
ce.career_set.create(career_type="coop", career="Full stack web developer")
ce.career_set.create(career_type="coop", career="Software developer")
ce.career_set.create(career_type="coop", career="Test automation developer")

# computer engineering fulltime
ce.career_set.create(career_type="fulltime", career="Network administrator")
ce.career_set.create(career_type="fulltime", career="Firmware engineer")
ce.career_set.create(career_type="fulltime", career="Software engineer")

# electrical engineering first-year courses
elec.course_set.create(course_type='first', course='ECE 102 - Information Session')
elec.course_set.create(course_type='first', course='MATH 117 - Calculus 1 for Engineering')
elec.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
elec.course_set.create(course_type='first', course='ECE 190 - Engineering Profession and Practice')
elec.course_set.create(course_type='first', course='ECE 150 - Fundamentals of Programming')
elec.course_set.create(course_type='first', course='ECE 105 - Classical Mechanics')
elec.course_set.create(course_type='first', course='GENE 191 - Communication in the Engineering Profession')
elec.course_set.create(course_type='first', course='MATH 119 - Calculus 2 for Engineering')
elec.course_set.create(course_type='first', course='ECE 192 - Engineering Economics and Impact on Society')
elec.course_set.create(course_type='first', course='ECE 140 - Linear Circuits')
elec.course_set.create(course_type='first', course='ECE 124 - Digital Circuits and Systems')
elec.course_set.create(course_type='first', course='ECE 108 - Discrete Mathematics and Logic 1')
elec.course_set.create(course_type='first', course='ECE 106 - Electricity and Magnetism')

# electrical engineering upper-year courses
elec.course_set.create(course_type='upper', course='ECE 406 – Algorithm Design and Analysis')
elec.course_set.create(course_type='upper', course='ECE 375 – Electromagnetic Fields and Waves')
elec.course_set.create(course_type='upper', course='ECE 309 – Introduction to Thermodynamics and Heat Transfer')
elec.course_set.create(course_type='upper', course='ECE 260 – Electromechanical Energy Conversion')

# electrical engineering coop
elec.career_set.create(career_type="coop", career="Hardware designer")
elec.career_set.create(career_type="coop", career="Electrical engineering intern")
elec.career_set.create(career_type="coop", career="Test systems engineering")
elec.career_set.create(career_type="coop", career="Artificial intelligence undergraduate researcher")
elec.career_set.create(career_type="coop", career="Assistant information analyst")
elec.career_set.create(career_type="coop", career="Hardware design engineer")

# electrical engineering fulltime
elec.career_set.create(career_type="fulltime", career="Engineering product manager")
elec.career_set.create(career_type="fulltime", career="Application specialist")
elec.career_set.create(career_type="fulltime", career="Software engineer")
elec.career_set.create(career_type="fulltime", career="Programmer")
elec.career_set.create(career_type="fulltime", career="Business technology analyst")
elec.career_set.create(career_type="fulltime", career="Electrical designer")
elec.career_set.create(career_type="fulltime", career="Hardware engineer")

# mechanical engineering first-year courses
mech.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
mech.course_set.create(course_type='first', course='GENE 123 - Electrical Circuits and Instrumentation')
mech.course_set.create(course_type='first', course='ME 115 - Structure and Properties of Materials')
mech.course_set.create(course_type='first', course='ME 101 - Introduction to Mechanical Engineering Practice 2')
mech.course_set.create(course_type='first', course='ME 100B - Seminar')
mech.course_set.create(course_type='first', course='PHYS 115 - Mechanics')
mech.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
mech.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
mech.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')
mech.course_set.create(course_type='first', course='ME 100 - Introduction to Mechanical Engineering Practice 1')

# mechanical engineering upper-year courses
mech.course_set.create(course_type='upper', course='ME 547 – Robot Manipulators: Kinematics, Dynamics, Control')
mech.course_set.create(course_type='upper', course='ME 435 – Industrial Metallurgy')
mech.course_set.create(course_type='upper', course='ME 321 – Kinematics and Dynamics of Machines')
mech.course_set.create(course_type='upper', course='ME 250 – Thermodynamics 1')

# mechanical engineering coop
mech.career_set.create(career_type="coop", career="Technical business analyst")
mech.career_set.create(career_type="coop", career="SQL application developer")
mech.career_set.create(career_type="coop", career="Product management associate")
mech.career_set.create(career_type="coop", career="Business systems analyst")
mech.career_set.create(career_type="coop", career="In-field data collection analyst")
mech.career_set.create(career_type="coop", career="Data scientist")
mech.career_set.create(career_type="coop", career="Business analyst")

# mechanical engineering fulltime
mech.career_set.create(career_type="fulltime", career="Supply chain logistics")
mech.career_set.create(career_type="fulltime", career="Senior hardware engineer")
mech.career_set.create(career_type="fulltime", career="Production engineer")
mech.career_set.create(career_type="fulltime", career="Quality control engineer")
mech.career_set.create(career_type="fulltime", career="Mechanical engineer")

# Biomedical engineering first-year courses
bmed.course_set.create(course_type='first', course='SYDE 114 - Numerical and Applied Calculus')
bmed.course_set.create(course_type='first', course='SYDE 112 - Fundamental Engineering Math 2')
bmed.course_set.create(course_type='first', course='BME 186 - Chemistry Principles')
bmed.course_set.create(course_type='first', course='BME 162 - Human Factors in the Design of Biomedical and Health Systems')
bmed.course_set.create(course_type='first', course='BME 122 - Data Structures and Algorithms')
bmed.course_set.create(course_type='first', course='BME 102 - Seminar')
bmed.course_set.create(course_type='first', course='SYDE 113 - Matrices and Linear Systems')
bmed.course_set.create(course_type='first', course='SYDE 111 - Fundamental Engineering Math 1')
bmed.course_set.create(course_type='first', course='BME 181 - Physics I - Statics')
bmed.course_set.create(course_type='first', course='BME 161 - Introduction to Biomedical Design')
bmed.course_set.create(course_type='first', course='BME 121 - Digital Computation')
bmed.course_set.create(course_type='first', course='BME 101/BME 101L - Communications in Biomedical Engineering')

# Biomedical engineering upper-year courses
bmed.course_set.create(course_type='upper', course='BME 450 – Sports Engineering')
bmed.course_set.create(course_type='upper', course='BME 386 – Physics of Medical Imaging')
bmed.course_set.create(course_type='upper', course='BME 361 – Biomedical Engineering Design')
bmed.course_set.create(course_type='upper', course='BME 261 – Prototype, Simulation and Design')

# Biomedical engineering coop
bmed.career_set.create(career_type="coop", career="Robotics and embedded sensor research assistant")
bmed.career_set.create(career_type="coop", career="Medical device design")
bmed.career_set.create(career_type="coop", career="Bioengineering research assistant")
bmed.career_set.create(career_type="coop", career="Signal processing algorithm developer")
bmed.career_set.create(career_type="coop", career="Medical device software developer")
bmed.career_set.create(career_type="coop", career="Junior biomedical engineer")

# Biomedical engineering fulltime
bmed.career_set.create(career_type="fulltime", career="Medical radiation therapist")
bmed.career_set.create(career_type="fulltime", career="Epidemiologist")
bmed.career_set.create(career_type="fulltime", career="Genetics technologist")
bmed.career_set.create(career_type="fulltime", career="Medical officer")
bmed.career_set.create(career_type="fulltime", career="Climate change information analyst")
bmed.career_set.create(career_type="fulltime", career="Microbiologist")

# System Design engineering first-year courses
syde.course_set.create(course_type='first', course='SYDE 223 - Data Structures and Algorithms')
syde.course_set.create(course_type='first', course='SYDE 192/192L - Digital Systems/Lab')
syde.course_set.create(course_type='first', course='SYDE 162 - Human Factors in Design')
syde.course_set.create(course_type='first', course='SYDE 114 - Numerical and Applied Calculus')
syde.course_set.create(course_type='first', course='SYDE 112 - Fundamental Engineering Math 2')
syde.course_set.create(course_type='first', course='SYDE 102 - Seminar')
syde.course_set.create(course_type='first', course='SYDE 181 - Physics 1')
syde.course_set.create(course_type='first', course='SYDE 161 - Introduction to Design')
syde.course_set.create(course_type='first', course='SYDE 121 - Digital Computation')
syde.course_set.create(course_type='first', course='SYDE 113 - Matrices and Linear Systems')
syde.course_set.create(course_type='first', course='SYDE 111 - Fundamental Engineering Math 1')
syde.course_set.create(course_type='first', course='SYDE 101/SYDE 101L - Communications in Systems Design Engineering')

# System Design engineering upper-year courses
syde.course_set.create(course_type='upper', course='SYDE 544 – Biomedical Measurement and Signal Processing')
syde.course_set.create(course_type='upper', course='SYDE 411 – Optimization and Numerical Methods')
syde.course_set.create(course_type='upper', course='SYDE 351 – Systems Models 1')
syde.course_set.create(course_type='upper', course='SYDE 286 – Mechanics of Deformable Solids')

# System Design engineering coop
syde.career_set.create(career_type="coop", career="Machine learning developer")
syde.career_set.create(career_type="coop", career="Control systems software designer co-op")
syde.career_set.create(career_type="coop", career="Application developer")
syde.career_set.create(career_type="coop", career="User experience designer")
syde.career_set.create(career_type="coop", career="Product manager")
syde.career_set.create(career_type="coop", career="Rapid prototype software developer")
syde.career_set.create(career_type="coop", career="Product design/development")

# System Design engineering fulltime
syde.career_set.create(career_type="fulltime", career="Energy manager")
syde.career_set.create(career_type="fulltime", career="Software engineer")
syde.career_set.create(career_type="fulltime", career="Applications engineer")
syde.career_set.create(career_type="fulltime", career="Senior solutions engineer")
syde.career_set.create(career_type="fulltime", career="Hardware program manager")
syde.career_set.create(career_type="fulltime", career="Software development engineer")

# Geological engineering first-year courses
geo.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
geo.course_set.create(course_type='first', course='GENE 123 - Electrical Circuits and Instrumentation')
geo.course_set.create(course_type='first', course='GEOE 153 - Earth Engineering')
geo.course_set.create(course_type='first', course='GEOE 121 - Computational Methods')
geo.course_set.create(course_type='first', course='CIVE 105 - Mechanics 2')
geo.course_set.create(course_type='first', course='ENGL 191/SPCOM 191 - Communication in the Engineering Profession')
geo.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
geo.course_set.create(course_type='first', course='GEOE 115 - Linear Algebra')
geo.course_set.create(course_type='first', course='CIVE 104 - Mechanics 1')
geo.course_set.create(course_type='first', course='GEOE 100 - Environmental and Geological Engineering Concepts')
geo.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')

# Geological engineering upper-year courses
geo.course_set.create(course_type='upper', course='EARTH 458 – Physical Hydrogeology')
geo.course_set.create(course_type='upper', course='CIVE 353 – Geotechnical Engineering 1')
geo.course_set.create(course_type='upper', course='ENVE 223 – Differential Equations and Balance Laws')
geo.course_set.create(course_type='upper', course='EARTH 238 – Introductory Structural Geology')

# Geological engineering coop
geo.career_set.create(career_type="coop", career="Geotechnical and materials technician")
geo.career_set.create(career_type="coop", career="Water/wastewater project assistant")
geo.career_set.create(career_type="coop", career="Rock mechanics assistant")
geo.career_set.create(career_type="coop", career="Mining/energy engineering student")
geo.career_set.create(career_type="coop", career="Industrial buildings inspector")
geo.career_set.create(career_type="coop", career="Project coordinator")
geo.career_set.create(career_type="coop", career="Field engineer")
geo.career_set.create(career_type="coop", career="Geotechnical engineering assistant")

# Geological engineering fulltime
geo.career_set.create(career_type="fulltime", career="Junior program engineer")
geo.career_set.create(career_type="fulltime", career="Geotechnical engineer")
geo.career_set.create(career_type="fulltime", career="Water specialist")
geo.career_set.create(career_type="fulltime", career="Rock mechanics engineer")
geo.career_set.create(career_type="fulltime", career="Geotechnical designer")
geo.career_set.create(career_type="fulltime", career="Geological engineer")

# School of Architecture first-year courses
arch.course_set.create(course_type='first', course='ARCH 173 - Building Construction 2')
arch.course_set.create(course_type='first', course='ARCH 143 – Ancient Worlds and Foundations of Europe')
arch.course_set.create(course_type='first', course='ARCH 126 – Environmental Building Design')
arch.course_set.create(course_type='first', course='ARCH 113 – Visual and Digital Media 2')
arch.course_set.create(course_type='first', course='ARCH 193 - Design Studio')
arch.course_set.create(course_type='first', course='ARCH 172 - Building Construction 1')
arch.course_set.create(course_type='first', course='ARCH 142 – Introduction to Cultural History')
arch.course_set.create(course_type='first', course='ARCH 120 - An Introduction to Architectural Ideas and Communications')
arch.course_set.create(course_type='first', course='ARCH 110 – Visual and Digital Media 1')
arch.course_set.create(course_type='first', course='ARCH 192 - Design Studio')

# School of Architecture upper-year courses
arch.course_set.create(course_type='upper', course='ARCH 465 – Advanced Structures: Design and Analysis')
arch.course_set.create(course_type='upper', course='ARCH 313 – Advanced Visualization and Analysis')
arch.course_set.create(course_type='upper', course='ARCH 327 – Architecture of the Urban Environment')
arch.course_set.create(course_type='upper', course='ARCH 246 – Pre-Renaissance to Reformation')

# School of Architecture coop
arch.career_set.create(career_type="coop", career="3D architectural visualization artist")
arch.career_set.create(career_type="coop", career="Architectural designer")
arch.career_set.create(career_type="coop", career="Intern architect")
arch.career_set.create(career_type="coop", career="Architectural student")
arch.career_set.create(career_type="coop", career="Architectural assistant")

# School of Architecture fulltime
arch.career_set.create(career_type="fulltime", career="Product designer")
arch.career_set.create(career_type="fulltime", career="Urban designer")
arch.career_set.create(career_type="fulltime", career="Project manager")
arch.career_set.create(career_type="fulltime", career="Associate architect")

# Architectural engineering first-year courses
arche.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
arche.course_set.create(course_type='first', course='GENE 123 - Electrical Circuits and Instrumentation')
arche.course_set.create(course_type='first', course='AE 125 - Architectural Graphics Studio')
arche.course_set.create(course_type='first', course='AE 121 - Computational Methods')
arche.course_set.create(course_type='first', course='AE 105 - Mechanics 2')
arche.course_set.create(course_type='first', course='MATH 116 Calculus 1 for Engineering')
arche.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')
arche.course_set.create(course_type='first', course='AE 115 - Linear Algebra')
arche.course_set.create(course_type='first', course='AE 104 - Mechanics 1')
arche.course_set.create(course_type='first', course='AE 101 - History of the Built Environment')
arche.course_set.create(course_type='first', course='AE 100 - Concepts Studio')

# Architectural engineering upper-year courses
arche.course_set.create(course_type='upper', course='AE 392 – Economics and Life Cycle Analysis')
arche.course_set.create(course_type='upper', course='AE 315 – Building Structural Systems')
arche.course_set.create(course_type='upper', course='AE 300 – Architectural Engineering Studio')
arche.course_set.create(course_type='upper', course='AE 265 – Structure and Properties of Materials')

# Architectural engineering coop
arche.career_set.create(career_type="coop", career="Building owners and operators")
arche.career_set.create(career_type="coop", career="Regulatory agencies")
arche.career_set.create(career_type="coop", career="Construction companies and developers")
arche.career_set.create(career_type="coop", career="Building performance consulting firms")
arche.career_set.create(career_type="coop", career="Consulting firms specializing in structural and/or architectural design")

# Environmental engineering first-year courses
env.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
env.course_set.create(course_type='first', course='GENE 123 - Electrical Circuits and Instrumentation')
env.course_set.create(course_type='first', course='ENVE 153 - Earth Engineering')
env.course_set.create(course_type='first', course='ENVE 121 - Computational Methods')
env.course_set.create(course_type='first', course='CIVE 105 - Mechanics 2')
env.course_set.create(course_type='first', course='ENGL 191/SPCOM 191 - Communication in the Engineering Profession')
env.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
env.course_set.create(course_type='first', course='ENVE 115 - Linear Algebra')
env.course_set.create(course_type='first', course='CIVE 104 - Mechanics 1')
env.course_set.create(course_type='first', course='ENVE 100 - Environmental and Geological Engineering Concepts')
env.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')

# Environmental engineering upper-year courses
env.course_set.create(course_type='upper', course='ENVE 391 – Law and Ethics for Environmental Engineers')
env.course_set.create(course_type='upper', course='ENVE 376 – Biological Processes')
env.course_set.create(course_type='upper', course='ENVE 375 – Physico-Chemical Processes')
env.course_set.create(course_type='upper', course='ENVE 277 – Air Quality Engineering')

# Environmental engineering coop
env.career_set.create(career_type="coop", career="Program developer")
env.career_set.create(career_type="coop", career="Industrial wastewater engineering")
env.career_set.create(career_type="coop", career="Project coordinator")
env.career_set.create(career_type="coop", career="Field engineer")
env.career_set.create(career_type="coop", career="Tides and water levels assistant")
env.career_set.create(career_type="coop", career="Technical writer")
env.career_set.create(career_type="coop", career="Environmental engineering assistant")
env.career_set.create(career_type="coop", career="Drainage design engineering assistant")

# Environmental engineering fulltime
env.career_set.create(career_type="fulltime", career="Water resource engineer")
env.career_set.create(career_type="fulltime", career="Operations specialist")
env.career_set.create(career_type="fulltime", career="Geomatics analyst")
env.career_set.create(career_type="fulltime", career="Project coordinator")
env.career_set.create(career_type="fulltime", career="Environmental specialist")
env.career_set.create(career_type="fulltime", career="Water resources specialist")
env.career_set.create(career_type="fulltime", career="Environmental consultant")

# Nanotechnology engineering first-year courses
nano.course_set.create(course_type='first', course='MATH 119 - Calculus 2 for Engineering')
nano.course_set.create(course_type='first', course='NE 131 - Physics for Nanotechnology Engineering')
nano.course_set.create(course_type='first', course='NE 125 - Introduction to Materials Science and Engineering')
nano.course_set.create(course_type='first', course='NE 140 - Linear Circuits')
nano.course_set.create(course_type='first', course='NE 113 - Introduction to Computational Methods')
nano.course_set.create(course_type='first', course='NE 102 - Introduction to Nanomaterials Health Risk; Nanotechnology Engineering Practice')
nano.course_set.create(course_type='first', course='MATH 117 - Calculus 1 for Engineering')
nano.course_set.create(course_type='first', course='NE 121 - Chemical Principles')
nano.course_set.create(course_type='first', course='NE 112 - Linear Algebra for Nanotechnology Engineering')
nano.course_set.create(course_type='first', course='NE 111 – Introduction to Programming for Engineers')
nano.course_set.create(course_type='first', course='NE 109 – Societal and Environmental Impacts of Nanotechnology')
nano.course_set.create(course_type='first', course='NE 101 - Nanotechnology Engineering Practice')
nano.course_set.create(course_type='first', course='NE 100 - Introduction to Nanotechnology Engineering')

# Nanotechnology engineering upper-year courses
nano.course_set.create(course_type='upper', course='NE 481 – Nanomedicine and Nanobiology')
nano.course_set.create(course_type='upper', course='NE 471 – Nano-electronics')
nano.course_set.create(course_type='upper', course='NE 336 – Micro and Nanosystem Computer-aided Design')
nano.course_set.create(course_type='upper', course='NE 225 – Structure and Properties of Nanomaterials')

# Nanotechnology engineering coop
nano.career_set.create(career_type="coop", career="Food technologist")
nano.career_set.create(career_type="coop", career="Quality project coordinator")
nano.career_set.create(career_type="coop", career="Optical development engineering")
nano.career_set.create(career_type="coop", career="Material handler")
nano.career_set.create(career_type="coop", career="Laboratory research assistant")
nano.career_set.create(career_type="coop", career="Research & development engineering")
nano.career_set.create(career_type="coop", career="Polymer engineering intern")

# Nanotechnology engineering fulltime
nano.career_set.create(career_type="fulltime", career="Research engineer")
nano.career_set.create(career_type="fulltime", career="Data scientist")
nano.career_set.create(career_type="fulltime", career="Product manager")
nano.career_set.create(career_type="fulltime", career="Project engineer specialist")
nano.career_set.create(career_type="fulltime", career="Engineering program manager")
nano.career_set.create(career_type="fulltime", career="Device development engineer")

# Management engineering first-year courses
msci.course_set.create(course_type='first', course='MSCI 131 – Work Design and Facilities Planning')
msci.course_set.create(course_type='first', course='MSCI 121 - Introduction to Computer Programming')
msci.course_set.create(course_type='first', course='PHYS 125 - Physics for Engineers')
msci.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
msci.course_set.create(course_type='first', course='GENE 123 - Electrical Circuits and Instrumentation')
msci.course_set.create(course_type='first', course='ENGL 192/SPCOM 192 - Communication in the Engineering Profession')
msci.course_set.create(course_type='first', course='MSCI 100B - Seminar')
msci.course_set.create(course_type='first', course='PHYS 115 - Mechanics')
msci.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
msci.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
msci.course_set.create(course_type='first', course='MSCI 100 - Management Engineering Concepts')
msci.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')

# Management engineering upper-year courses
msci.course_set.create(course_type='upper', course='MSCI 333 – Simulation Analysis and Design')
msci.course_set.create(course_type='upper', course='MSCI 332 – Deterministic Optimization Models and Methods')
msci.course_set.create(course_type='upper', course='MSCI 311 – Organizational Design and Technology')
msci.course_set.create(course_type='upper', course='MSCI 343 – Human-Computer Interaction')

# Management engineering coop
msci.career_set.create(career_type="coop", career="Technical business analyst")
msci.career_set.create(career_type="coop", career="SQL application developer")
msci.career_set.create(career_type="coop", career="Product management associate")
msci.career_set.create(career_type="coop", career="Business systems analyst")
msci.career_set.create(career_type="coop", career="Supply chain logistics")
msci.career_set.create(career_type="coop", career="In-field data collection analyst")
msci.career_set.create(career_type="coop", career="Data scientist")
msci.career_set.create(career_type="coop", career="Business analyst")

# Management engineering fulltime
msci.career_set.create(career_type="fulltime", career="Applications developer")
msci.career_set.create(career_type="fulltime", career="Software developer")
msci.career_set.create(career_type="fulltime", career="User experience researcher")
msci.career_set.create(career_type="fulltime", career="Software engineer")
msci.career_set.create(career_type="fulltime", career="Technical consultant")
msci.career_set.create(career_type="fulltime", career="Data scientist")
msci.career_set.create(career_type="fulltime", career="Supply chain analyst")
msci.career_set.create(career_type="fulltime", career="Project coordinator")
msci.career_set.create(career_type="fulltime", career="Business systems analyst")

# Civil engineering first-year courses
cive.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
cive.course_set.create(course_type='first', course='GENE 123 - Electrical Engineering')
cive.course_set.create(course_type='first', course='CIVE 199 - Seminar')
cive.course_set.create(course_type='first', course='CIVE 153 - Earth Engineering')
cive.course_set.create(course_type='first', course='CIVE 121 - Computational Methods')
cive.course_set.create(course_type='first', course='CIVE 105 - Mechanics 2')
cive.course_set.create(course_type='first', course='ENGL 191/SPCOM 191 - Communication in the Engineering Profession')
cive.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
cive.course_set.create(course_type='first', course='CIVE 115 - Linear Algebra')
cive.course_set.create(course_type='first', course='CIVE 104 - Mechanics 1')
cive.course_set.create(course_type='first', course='CIVE 100 - Civil Engineering Concepts')
cive.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')

# Civil engineering upper-year courses
cive.course_set.create(course_type='upper', course='CIVE 460 – Engineering Biomechanics')
cive.course_set.create(course_type='upper', course='CIVE 332 – Civil Systems and Project Management')
cive.course_set.create(course_type='upper', course='CIVE 310 – Introduction to Structural Design')
cive.course_set.create(course_type='upper', course='CIVE 241 – Transport Principles and Applications')

# Civil engineering coop
cive.career_set.create(career_type="coop", career="Structural engineering student")
cive.career_set.create(career_type="coop", career="Project manager")
cive.career_set.create(career_type="coop", career="Estimator")
cive.career_set.create(career_type="coop", career="Concrete lab technician")
cive.career_set.create(career_type="coop", career="Transportation planner")
cive.career_set.create(career_type="coop", career="Diagnostics civil engineer")
cive.career_set.create(career_type="coop", career="Quality control technician")
cive.career_set.create(career_type="coop", career="Field technician")

# Civil engineering fulltime
cive.career_set.create(career_type="fulltime", career="Project manager")
cive.career_set.create(career_type="fulltime", career="Civil engineer")
cive.career_set.create(career_type="fulltime", career="Field engineer")
cive.career_set.create(career_type="fulltime", career="Structural design engineer")
cive.career_set.create(career_type="fulltime", career="Structural engineer")
cive.career_set.create(career_type="fulltime", career="Tunnel engineer")

# Software engineering first-year courses
swe.course_set.create(course_type='first', course='SE 102 - Seminar')
swe.course_set.create(course_type='first', course='MATH 119 - Calculus 2 for Engineering')
swe.course_set.create(course_type='first', course='ECE 140 - Linear Circuits')
swe.course_set.create(course_type='first', course='ECE 124 - Digital Circuits and Systems')
swe.course_set.create(course_type='first', course='ECE 106 - Electricity and Magnetism')
swe.course_set.create(course_type='first', course='CS 138 - Introduction to Data Abstraction and Implementation')
swe.course_set.create(course_type='first', course='SE 101 - Introductions to Methods of Software Engineering')
swe.course_set.create(course_type='first', course='MATH 135 - Algebra for Honours Mathematics')
swe.course_set.create(course_type='first', course='MATH 117 - Calculus 1 for Engineering')
swe.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
swe.course_set.create(course_type='first', course='ECE 105 - Classical Mechanics')
swe.course_set.create(course_type='first', course='CS 137 - Programming Principles')

# Software engineering upper-year courses
swe.course_set.create(course_type='upper', course='SE 465 – Software Testing and Quality Assurance')
swe.course_set.create(course_type='upper', course='SE 350 – Operating Systems')
swe.course_set.create(course_type='upper', course='SE 464 – Software Design and Architectures')
swe.course_set.create(course_type='upper', course='SE 212 – Logic and Computation')

# Software engineering coop
swe.career_set.create(career_type="coop", career="Algorithms engineering")
swe.career_set.create(career_type="coop", career="Production engineering")
swe.career_set.create(career_type="coop", career="iOS developer")
swe.career_set.create(career_type="coop", career="Software developer")
swe.career_set.create(career_type="coop", career="Mobile developer")
swe.career_set.create(career_type="coop", career="Data scientist")
swe.career_set.create(career_type="coop", career="Tools and automation engineering intern")

# Software engineering fulltime
swe.career_set.create(career_type="fulltime", career="Senior software engineer")
swe.career_set.create(career_type="fulltime", career="Web development engineer")
swe.career_set.create(career_type="fulltime", career="Innovation specialist")
swe.career_set.create(career_type="fulltime", career="Software developer")
swe.career_set.create(career_type="fulltime", career="Software development engineer")
swe.career_set.create(career_type="fulltime", career="Software engineer")

# Mechatronics engineering first-year courses
tron.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
tron.course_set.create(course_type='first', course='MTE 140 - Algorithms and Data Structures')
tron.course_set.create(course_type='first', course='MTE 120 - Circuits')
tron.course_set.create(course_type='first', course='MTE 119 - Statics')
tron.course_set.create(course_type='first', course='MTE 111 - Structure and Properties of Materials')
tron.course_set.create(course_type='first', course='MTE 100B – Seminar')
tron.course_set.create(course_type='first', course='GENE 121 - Digital Computation')
tron.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
tron.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
tron.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')
tron.course_set.create(course_type='first', course='MTE 100 - Mechatronics Engineering')

# Mechatronics engineering upper-year courses
tron.course_set.create(course_type='upper', course='MTE 544 – Autonomous Mobile Robots')
tron.course_set.create(course_type='upper', course='MTE 322 – Electromechanical Machine Design')
tron.course_set.create(course_type='upper', course='MTE 220 – Sensors and Instrumentation')
tron.course_set.create(course_type='upper', course='MTE 262 – Introduction to Microprocessors and Digital Logic')

# Mechatronics engineering coop
tron.career_set.create(career_type="coop", career="Application developer")
tron.career_set.create(career_type="coop", career="Product manager")
tron.career_set.create(career_type="coop", career="Instrumental engineering")
tron.career_set.create(career_type="coop", career="Control systems software design")
tron.career_set.create(career_type="coop", career="Mechanical designer-automation")
tron.career_set.create(career_type="coop", career="Hardware engineering intern")
tron.career_set.create(career_type="coop", career="Robotics software developer")
tron.career_set.create(career_type="coop", career="Systems software engineering")

# Mechatronics engineering fulltime
tron.career_set.create(career_type="fulltime", career="Reactor designer")
tron.career_set.create(career_type="fulltime", career="Android partner engineer")
tron.career_set.create(career_type="fulltime", career="Mechanical engineer")
tron.career_set.create(career_type="fulltime", career="Program manager")
tron.career_set.create(career_type="fulltime", career="Firmware engineer")
tron.career_set.create(career_type="fulltime", career="iPhone product design engineer")
tron.career_set.create(career_type="fulltime", career="Telematics engineer")
tron.career_set.create(career_type="fulltime", career="Systems engineer")

# Chemical engineering first-year courses
chem.course_set.create(course_type='first', course='PHYS 115 - Mechanics')
chem.course_set.create(course_type='first', course='MATH 118 - Calculus 2 for Engineering')
chem.course_set.create(course_type='first', course='CHE 181 - Design Studio 2')
chem.course_set.create(course_type='first', course='CHE 161 - Engineering Biology')
chem.course_set.create(course_type='first', course='CHE 101 - Chemical Engineering Concepts 2')
chem.course_set.create(course_type='first', course='MATH 116 - Calculus 1 for Engineering')
chem.course_set.create(course_type='first', course='MATH 115 - Linear Algebra for Engineering')
chem.course_set.create(course_type='first', course='CHE 180 - Design Studio 1')
chem.course_set.create(course_type='first', course='CHE 120 - Computer Literacy and Programming for Chemical Engineers')
chem.course_set.create(course_type='first', course='CHE 102 - Chemistry for Engineers')
chem.course_set.create(course_type='first', course='CHE 100 - Chemical Engineering Concepts 1')

# Chemical engineering upper-year courses
chem.course_set.create(course_type='upper', course='CHE 571 – Industrial Ecology')
chem.course_set.create(course_type='upper', course='CHE 425 – Strategies for Process Improvement and Product Development')
chem.course_set.create(course_type='upper', course='CHE 361 – Bioprocess Engineering')
chem.course_set.create(course_type='upper', course='CHE 241 – Materials Science and Engineering')

# Chemical engineering coop
chem.career_set.create(career_type="coop", career="Supply chain assistant")
chem.career_set.create(career_type="coop", career="Process analyst")
chem.career_set.create(career_type="coop", career="Quality project coordinator")
chem.career_set.create(career_type="coop", career="Production coordinator")
chem.career_set.create(career_type="coop", career="Reliability engineer")
chem.career_set.create(career_type="coop", career="Data analyst")
chem.career_set.create(career_type="coop", career="Continuous improvement engineer")
chem.career_set.create(career_type="coop", career="Manufacturing engineer")

# Chemical engineering fulltime
chem.career_set.create(career_type="fulltime", career="Project engineer")
chem.career_set.create(career_type="fulltime", career="Process specialist")
chem.career_set.create(career_type="fulltime", career="Production engineer")
chem.career_set.create(career_type="fulltime", career="Engineering coordinator")
chem.career_set.create(career_type="fulltime", career="Quality specialist")
chem.career_set.create(career_type="fulltime", career="Process engineer")

# Comparisons
ce.program.create(program_2="Software Engineering", comparison="The three programs have common elements: they all stress an understanding of both digital hardware and software, though to varying degrees, and they all hone students' problem-solving skills. As well, graduates of all three programs may compete for some of the same jobs. However, the programs have different objectives. Computer Engineering (CE) deals with designing, developing, and operating computer systems. At its core, Computer Engineering concentrates on digital hardware devices and computers, and the software that controls them. Advanced courses focus on standard designs and techniques for specific application domains. In contrast to CS and SE, Computer Engineering emphasizes solving problems in digital hardware and at the hardware-software interface. Computer Science (CS) focuses on understanding, designing, and developing programs and computers. At its core, Computer Science concentrates on data, data transformation, and algorithms. Advanced courses present specialized programming techniques and specific application domains. The CS program is less structured than the CE and SE programs, giving students more flexibility to build depth or breadth in a variety of application domains or in the fundamentals of Computer Science. Software Engineering (SE) deals with building and maintaining software systems. It is more software-oriented and has a greater emphasis on large software applications than Computer Engineering. It is more applied than Computer Science, placing greater emphasis on the entire software development process, from idea to final product. It is also more disciplined than Computer Science, applying more systematic practices to help ensure that products are reliable and safe.")
msci.program.create(program_2="System Design Engineering", comparison="While systems design engineering covers some similar topics such as scheduling and optimisation, ergonomics, information management and project management, they have a stronger focus on the design of mechanical and electrical systems, placing more emphasis on product design and development. Management engineers typically work at the next higher level of analysis and solution design; more emphasis is placed on optimisation and system efficiency. Compared to systems design engineering, management engineering contains a lot more courses in supply chain management and information technologies.")
msci.program.create(program_2="Software Engineering", comparison="Software Engineering applies computer science and engineering to the design of software systems. Software Engineering students take a large number of computer science and computer engineering courses at the interface of digital hardware and software, as well as core software engineering courses on software development. In contrast, Management Engineers design, implement, and manage complex management systems. Increasingly, those management systems are implemented as software and information systems. Therefore, information/software systems design comprises a major theme area in Management Engineering, with a number of courses falling in the areas of computer science, software engineering, and information systems. In this regard, of the 13 other engineering programs offered at the University of Waterloo, only the Software Engineering and Computer Engineering programs have more such courses in their core curriculum. While Management Engineering students learn how to design and build basic information systems, they do not get training in low-level systems programming. For example, a software engineering student will learn about real time systems, concurrent programming, and operating systems while Management Engineering students will not have any exposure to these topics. Likewise, Software Engineering students do not learn about important application areas of Management Engineering such as supply chain management, operations planning, and inventory control nor do Software Engineering students learn fundamental methods such as stochastics, simulation, and optimization as part of their core curriculum. Simply put, Management Engineering students learn to solve large real-world problems of businesses and organizations that are implemented in software, while Software Engineering students learn to solve a wide range of software problems including low-level systems programming.")
swe.program.create(program_2="Computer Engineering", comparison="The three programs have common elements: they all stress an understanding of both digital hardware and software, though to varying degrees, and they all hone students' problem-solving skills. As well, graduates of all three programs may compete for some of the same jobs. However, the programs have different objectives. Computer Engineering (CE) deals with designing, developing, and operating computer systems. At its core, Computer Engineering concentrates on digital hardware devices and computers, and the software that controls them. Advanced courses focus on standard designs and techniques for specific application domains. In contrast to CS and SE, Computer Engineering emphasizes solving problems in digital hardware and at the hardware-software interface. Computer Science (CS) focuses on understanding, designing, and developing programs and computers. At its core, Computer Science concentrates on data, data transformation, and algorithms. Advanced courses present specialized programming techniques and specific application domains. The CS program is less structured than the CE and SE programs, giving students more flexibility to build depth or breadth in a variety of application domains or in the fundamentals of Computer Science. Software Engineering (SE) deals with building and maintaining software systems. It is more software-oriented and has a greater emphasis on large software applications than Computer Engineering. It is more applied than Computer Science, placing greater emphasis on the entire software development process, from idea to final product. It is also more disciplined than Computer Science, applying more systematic practices to help ensure that products are reliable and safe.")
syde.program.create(program_2="Management Engineering", comparison="Industrial engineering traditionally focuses on the application of engineering methods for the improvement of manufacturing and industry-related processes, but has broadened to include other work-related domains such as health care and information management. This is the focus of Waterloo’s management engineering program, which is offered by our Department of Management Sciences. Systems design engineering includes many industrial engineering methods as part of its core curriculum, such as scheduling and optimization, human factors and ergonomics, information management, and project management, which are applied in students’ first-year team design projects. However, our students also learn the basics of the mechanical, electrical, computing, civil, and software engineering disciplines, which enables them to determine where they focus their studies in upper years.")
syde.program.create(program_2="Software Engineering", comparison="Programs in computer engineering and systems engineering focus almost exclusively on computing systems (hardware/software), while Systems Design covers a much wider variety of systems that may or may not include computing systems. Similarly, Waterloo’s software engineering program focuses almost exclusively on software development. Many systems design students find themselves in software-oriented (programming) type jobs, especially during early work terms. However, our students are not bound to follow an exclusively computer or software-oriented path. Students take approximately one computer-based course per term for the first two years of study, after which they may choose to take electives that are related to computers and software, or concentrate on areas such as human-ergonomic and societal-environmental systems. Senior design projects cover a wide range of applications, environmental systems modeling, conflict analysis, pattern recognition, intelligent systems, human-computer interaction, and biomechanics.")
syde.program.create(program_2="Mechatronics Engineering", comparison="In systems design engineering, the focus in the early semesters is on building up a base of general engineering knowledge, as well as knowledge and experience with design methodology that can be applied broadly. Students can then take technical electives and work on advanced design projects in areas that are of particular interest to them, such as mechatronics, intelligent systems, human-computer interaction, systems modelling, and alternative energy. In contrast, the mechatronics engineering program focuses specifically on the design of effective mechatronic systems that combine mechanical, electronic, computer, and software concepts, such as robotics, vehicular systems, and “smart” devices. For students interested in both the broad application of design and mechatronic systems, the best approach may be to combine the Systems Design program with a Mechatronics Option.")
arche.program.create(program_2="Civil Engineering", comparison="The Architectural Engineering program will focus heavily on building design. In contrast, Civil Engineering is a more general field with more breadth. The Civil Engineering curriculum includes design of all large municipal infrastructure components. Students in both programs will take courses in structural analysis and design (i.e. how to determine forces in structures and size their members, connections, etc.). Architectural Engineering students will also take courses on building science and systems, such as HVAC, in the place of courses that Civil Engineering students take on transportation networks, water distribution systems, geotechnical engineering and more. Architectural Engineering students will be able to work for design consulting firms specializing in the design, construction, renovation and rehabilitation of buildings. Civil Engineers are more likely to get jobs with municipalities, provincial highway authorities and construction companies. There is certainly some overlap between these programs. However, the Architectural Engineering program has been developed to address highly specified issues particular to building construction.")
arche.program.create(program_2="School of Architechture", comparison="The Architectural Engineering program will be an accredited engineering program, so graduates will be able to start working towards P.Eng status. Course content-wise, the program is actually closer to Civil Engineering than Architecture. Courses will cover content on mechanics, structural analysis and structural design, as well as heavy math content in the first two years. Architectural Engineering graduates will have a better understanding of the science and engineering behind good building design – not just the structural aspects, but also energy efficiency, sustainable building design and smart/green building design. Architectural Engineering only covers enough about the aesthetic aspects of building design to be able to communicate intelligently with architects in their own language on this subject. In Architecture, these aesthetic aspects are a much greater focus.")
arch.program.create(program_2="Architectural Engineering", comparison="If you're strong in artistic and creative abilities and have a background in math and science, Architecture is for you. You'll focus on design that applies social and cultural aspects as well as science and engineering to construction projects, ranging from accessible public space to environmental approaches to sustainable building and landscape and urban design. Architectural Engineering is closer to Civil Engineering than it is to Architecture. Students will cover mechanics, structural analysis, structural design, and in the first two years, a lot of math. You'll learn about the science and engineering behind good building design – not just the structural aspects, but also energy efficiency, sustainable building design, and smart/green building design.")
