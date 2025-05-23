import Link from "next/link";
import "./home.css";
export default function HomePage() {
  return (
    <>
      <div className="min-h-[82vh] h-[82vh]">
        <section className="px-1  h-full">
          <div className="flex flex-col justify-evenly items-center h-full">
            <div className=" flex flex-col items-center gap-8">
              <h1 className=" font-extrabold py-5 text-2xl multi-color-effect 2xl:text-4xl">
                AI-Powered Solar Panel Fault Detection
              </h1>
              <p className=" pl-5 pr-3 text-justify font-bold text-xl">Welcome to the Solar Panel Fault Detection System, an advanced AI-powered tool designed to help you maintain your solar panels effortlessly.</p>
            </div>
            <div className="flex gap-5">
              <Link href="/app">
                <button className=" border dark:border-none py-2 px-4 rounded-xl font-semibold dark:bg-green-500 dark:hover:text-black">
                  Try Now
                </button>
              </Link>
              <Link href="/about">
                <button className=" border dark:border-none py-2 px-4 rounded-xl font-semibold dark:bg-green-500 dark:hover:text-black">
                  Learn More..
                </button>
              </Link>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}
