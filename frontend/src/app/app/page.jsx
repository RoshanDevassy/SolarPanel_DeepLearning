import ImageUploader from "@/components/ImageUpload";


export const metadata = {
  title: "Solar Guard AI: APP",
  description: "Solar Panel Fault Detection System App.",
};

export default function App() {

  return (
    <>
      <div className=" min-h-[82vh] flex justify-center items-center">
        <ImageUploader />
      </div>
    </>
  );
}
