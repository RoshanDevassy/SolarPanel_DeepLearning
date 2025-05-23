import Link from "next/link";

export default function Navbar() {
  const navObj = [
    {
      id: 1,
      linkName: "Home",
      linkHref: "/",
    },
    {
      id: 2,
      linkName: "About",
      linkHref: "/about",
    },
    {
      id: 3,
      linkName: "App",
      linkHref: "/app",
    },
    {
      id: 4,
      linkName: "Help",
      linkHref: "/help",
    },
  ];

  return (
    <>
      <nav className="flex bg-slate-800 flex-grow basis-full flex-shrink justify-center items-center">
        <div className="flex flex-grow flex-shrink basis-full justify-center items-center">
          <div className="flex gap-3">
            {navObj.map((val) => (
              <Link
                href={val.linkHref}
                key={val.id}
                className="px-2 py-1 rounded-lg hover:bg-slate-700 hover:cursor-pointer text-white"
              >
                {val.linkName}
              </Link>
            ))}
          </div>
        </div>
      </nav>
    </>
  );
}
