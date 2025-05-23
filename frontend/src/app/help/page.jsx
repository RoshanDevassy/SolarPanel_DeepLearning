

export const metadata = {
  title: "Solar Guard AI : Help",
  description: "Help in Solar Panel Fault Detection System",
};

export default function Help() {
  const useSteps = [
    {
      id: 1,
      step: "Click on the 'Choose File' Button",
      description: "Select a clear image of your solar panel.",
    },{
      id: 2,
      step: "Click on the 'Upload & Predict' Button",
      description: "The button changes to Processing state",
    },
    {
      id: 3,
      step: "Wait for AI Analysis",
      description:
        "Our system will process the image and detect potential faults.",
    },
    {
      id: 4,
      step: "View Results",
      description:
        "The app will display detected issues such as dust accumulation, cracks, or bird droppings.",
    },
    {
      id: 5,
      step: "Take Action",
      description:
        "Follow suggested maintenance tips to resolve the identified faults.",
    },
  ];

  return (
    <>
      <div className=" min-h-[82vh] p-1 pl-5 pr-3">
        <section className=" pb-3">
          <div>
            <h1 className=" c-main-heading-style">Help & Support</h1>
            <h3 className=" c-sub-heading-style">How to Use the App</h3>
            <p>
              Follow these simple steps to detect faults in your solar panel:
            </p>
            <ul className=" c-list-style">
              {useSteps.map((steps) => (
                <li key={steps.id}>
                  {steps.step} - {steps.description}
                </li>
              ))}
            </ul>
          </div>
        </section>
        <section className=" pb-3">
          <div>
            <h2 className=" c-sub-heading-style">
              Frequently Asked Questions (FAQs)
            </h2>
            <h3 className="c-sub-heading-style">
              What types of faults can this system detect?
            </h3>
            <p>Our AI model identifies issues like:</p>
            <ul className=" c-list-style">
              <li>Dust Accumulation</li>
              <li>Bird Droppings</li>
              <li>Physical damage (cracks, scratches, etc.)</li>
              <li>Snow Covered</li>
            </ul>
          </div>
        </section>
        <section className=" pb-3">
          <div>
            <h3 className=" c-sub-heading-style">
              What if my image is blurry or unclear?
            </h3>
            <p>For accurate detection, ensure that:</p>
            <ul className=" c-list-style">
              <li>The image is well-lit and taken from a proper angle.</li>
              <li>The panel is fully visible in the image.</li>
              <li>The image is not too dark or overexposed.</li>
            </ul>
          </div>
        </section>
        <section className="pb-3">
          <div>
            <h3 className=" c-sub-heading-style">Can I use this on mobile devices?</h3>
            <p className=" text-justify">Yes, the web app is
              mobile-friendly. We are also working on a dedicated mobile app for
              better accessibility.</p>
          </div>
        </section>
        <section className=" pb-3">
          <div>
            <h2 className=" c-sub-heading-style">Troubleshooting Guide</h2>
            <h3 className=" c-sub-heading-style">Image is not uploading?</h3>
            <ul className=" c-list-style">
              <li>Ensure the image format is JPEG or PNG.</li>
              <li>Check your internet connection.</li>
              <li>Refresh the page and try again.</li>
            </ul>
          </div>
        </section>
        <section>
          <div>
            <h3 className=" c-sub-heading-style">Results seem inaccurate?</h3>
            <ul className=" c-list-style">
              <li>Use a clearer image with better lighting.</li>
              <li>Ensure the entire solar panel is captured.</li>
              <li>Try uploading a different image for better analysis.</li>
            </ul>
          </div>
        </section>
      </div>
    </>
  );
}
