import "./page.css";

export const metadata = {
  title: "Solar Guard AI : About",
  description: "About Solar Panel Fault Detection System",
};

export default function AboutPage() {
  const technologiesUsed = [
    {
      id: 1,
      t_type: "Frontend",
      description:
        "Built using Next.js and Tailwind CSS for a seamless user experience.",
    },
    {
      id: 2,
      t_type: "Backend",
      description: "Powered by FastAPI, a high-performance Python framework.",
    },
    {
      id: 3,
      t_type: "AI Model",
      description:
        "Developed using TensorFlow and trained on a diverse dataset to detect different solar panel faults.",
    },
    
  ];

  const featureScopes = [
    {
      id: 1,
      description:
        "Real-time IoT integration for continuous monitoring of solar panels.",
    },
    {
      id: 2,
      description:
        "Mobile App Support to make fault detection accessible from anywhere.",
    },
    {
      id: 3,
      description:
        "Enhanced AI Models to improve detection accuracy and cover more fault types.",
    },
    {
      id: 4,
      description:
        "Automated Maintenance Alerts to notify users when action is needed.",
    },
  ];

  return (
    <>
      <div className="min-h-[82vh] p-1 pl-5 pr-3">
        <section className=" pb-3">
          <div>
            <h1 className="c-main-heading-style">About Us</h1>
            <h3 className=" c-sub-heading-style">Introduction</h3>
            <p className=" text-justify">
              Welcome to the Solar Panel Fault Detection System, an AI-powered
              tool designed to help users detect faults in their solar panels
              with ease. Our goal is to provide an efficient, accurate, and
              user-friendly platform for identifying issues such as dust
              accumulation, bird droppings, and physical damage that may affect
              the performance of solar panels.
            </p>
          </div>
        </section>
        <section className="pb-3">
          <div>
            <h1 className="c-sub-heading-style">Why This Matters</h1>
            <p className=" text-justify">
              Solar panels are a significant investment, and maintaining their
              efficiency is crucial for maximizing energy output. Common issues
              like dirt buildup, cracks, or shading can reduce energy
              production, leading to financial losses. Our AI-driven solution
              ensures early fault detection, helping users take preventive
              action and improve the longevity of their solar panels.
            </p>
          </div>
        </section>
        <section className=" pb-3">
          <div>
            <h1 className=" c-sub-heading-style">Technology Used</h1>
            <p>
              Our platform leverages the latest advancements in web development
              and deep learning to deliver accurate fault detection results. The
              key technologies used include:
            </p>
            <ul className=" list-disc list-inside pl-1">
              {technologiesUsed.map((tech_used) => (
                <li key={tech_used.id}>
                  {tech_used.t_type} : {tech_used.description}
                </li>
              ))}
            </ul>
          </div>
        </section>
        <section>
          <div>
            <h1 className=" c-sub-heading-style">Future Scope</h1>
            <p>
              We aim to enhance our platform with additional features,
              including:
            </p>
            <ul className="c-list-style">
              {featureScopes.map((feature_scope) => (
                <li key={feature_scope.id}>{feature_scope.description}</li>
              ))}
            </ul>
          </div>
        </section>
      </div>
    </>
  );
}
